# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from resources import UserProfileResource
from models import UserProfile, Session, Progress, Stage, Route, RoutesCompleted, RouteProgress, Achievement, UserAchievement
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ObjectDoesNotExist
from haversine import haversine
from django.conf import settings

import json, datetime


def getSelf(request):
    if request.method == 'GET' and request.GET.get("deviceID"):
        res = UserProfileResource()
        request_bundle = res.build_bundle(request=request)
        queryset = res.obj_get_list(request_bundle)
        if queryset.count() > 0:
            user = res.obj_get(deviceID=request.GET.get("deviceID"), bundle=request_bundle)
            print user.pk
            user.id = user.pk
            bundle = res.build_bundle(obj=user, request=request)
            return HttpResponse(res.serialize(None, res.full_dehydrate(bundle), 
                                              'application/json'), 
                                mimetype="application/json")
        else:
            print "NOT FOUND"

        UserProfile.objects.get_or_create(deviceID=request.GET.get("deviceID"),
                                          defaults={'user':User.objects.create_user(request.GET.get("deviceID"))})[0]
        user = res.obj_get(deviceID=request.GET.get("deviceID"), bundle=request_bundle)
        bundle = res.build_bundle(obj=user, request=request)
        return HttpResponse(res.serialize(None, res.full_dehydrate(bundle), 
                                          'application/json'), 
                            mimetype="application/json")

    return HttpResponse('Unauthorized method', status=401)

@csrf_exempt
def startSession(request):
    if request.method == 'POST':
        body = json.loads(request.body)
        route = Route.objects.filter(pk=body['routeID'])[0]
        userID = UserProfile.objects.filter(pk=body['deviceID'])[0]
        # stage = Stage.objects.filter(pk=request.GET.get('stageID'))[0]
        print route
        startStage = None
        routeCompleted = RoutesCompleted.objects.get_or_create(routeID=route,
                                                               userID=userID)[0]
        if routeCompleted.currentJourney is None:
            progress = Progress(stageID=route.startStage,
                                userID=userID)
            progress.save()
            routeProgress = RouteProgress(progress=progress)
            routeProgress.save()
            routeProgress.allProgress.add(progress)
            routeProgress.save()
            routeCompleted.allJourneys.add(routeProgress)
            routeCompleted.currentJourney = routeProgress
            routeCompleted.save()
            
        routeProgress = routeCompleted.currentJourney
        progress = routeProgress.progress

        session = Session(userID=userID, routesCompleted=routeCompleted,
                          lastLat=float(body['lat']), lastLon=float(body['lon']),
                          lastTime=body['timestamp'])
        session.save()
        
        distance = routeCompleted.currentJourney.progress.totalDistance
        
                
        response = {}
        response['id'] = session.pk
        response['distance'] = distance
        response['distanceRemain'] = progress.stageID.distance - progress.totalDistance
        response['stageLength'] = progress.stageID.distance
        response['routeDistanceRemain'] = routeCompleted.routeID.length - routeProgress.distance
        response['routeLength'] = routeCompleted.routeID.length
        response['currentStage'] = routeProgress.progress.stageID.id
        response['totalTime'] = session.totalTime
        response['stageImage'] = session.routesCompleted.currentJourney.progress.stageID.image
        
        return HttpResponse(json.dumps(response), content_type="application/json")
    
    return HttpResponse("Unauthorized method", status=405)

@csrf_exempt
def updateSession(request):
    if request.method == 'PATCH':
        body = json.loads(request.body) 
        if all(k in body for k in ("sessionID", "lon", "lat", "timestamp")):
            try:
                session = Session.objects.get(id=body['sessionID'])
            except ObjectDoesNotExist:
                return HttpResponse("Session Not Found", status=404)
            
            if session.lastTime >= body['timestamp']:
                return HttpResponse("Timestamp of request too old", status=400)
            
            currentCoord = (float(session.lastLat), float(session.lastLon))
            nextCoord = (float(body['lat']), float(body['lon']))
            distance =  haversine(currentCoord, nextCoord) * 1000 # to get m not km
            
            timeIncrement = body['timestamp'] - session.lastTime
            
            # distance * 1000 since timeIncrement is in milliseconds
            if (distance * 1000 / timeIncrement) > settings.MAX_SPEED:
                distance = (settings.MAX_SPEED * timeIncrement) / 1000
                
            speed = distance * 1000 / timeIncrement

            session.distance = session.distance + distance
            session.lastLat = body['lat']
            session.lastLon = body['lon']
            session.totalTime = session.totalTime + timeIncrement
            session.lastTime = body['timestamp']

            session.userID.totalTime = session.userID.totalTime + timeIncrement
            session.userID.totalDistance = session.userID.totalDistance + distance
            session.userID.save()
            
            rc = session.routesCompleted
            rp = rc.currentJourney
            
            rp.time = rp.time + timeIncrement
            rp.save()
            
            progress = rp.progress
            payload = {}
            
            while (progress.totalDistance + distance >= progress.stageID.distance):
                difference = progress.stageID.distance - progress.totalDistance
                distance = distance - difference
                timeDifference = difference / (speed / 1000) # Time is in ms, speed is m/second
                timeIncrement = timeIncrement - timeDifference
                # print "Time Difference: {}".format(timeDifference)
                # print "Time Increment: {}".format(timeIncrement)
                if not (timeIncrement > 0):
                    timeIncrement = 0
                    timeDifference = 0

                rp.distance = rp.distance + difference
                # rp.time = rp.time + timeDifference
                session.stagesCompleted = session.stagesCompleted + 1
    
                progress.totalTime = progress.totalTime + timeDifference
                progress.completionDate = datetime.datetime.now()
                progress.totalDistance = progress.stageID.distance
                progress.completed = True
                progress.save()
                
                if (progress.stageID.nextStage is None):
                    rp.completed = True
                    rp.save()
                    if rc.bestTime == 0 or rc.bestTime > rp.time:
                        rc.bestTime = rp.time
                        achievements = Achievement.objects.filter(route=rc.routeID)
                        payload['achievements'] = []
                        for a in achievements:
                            if a.metric >= rc.bestTime:
                                obj, created = UserAchievement.objects.get_or_create(userID=rc.userID,
                                                                                     achievementID=a)
                                print "Created: {}".format(created)
                                if created:
                                    ach = {}
                                    ach['name'] = a.name
                                    ach['value'] = a.value
                                    payload['achievements'].append(ach)
                        # Add Award
                    rc.completed = True
                    progress = Progress(stageID=rc.routeID.startStage,
                                        userID=rc.userID)
                    progress.save()
                    rp = RouteProgress(progress=progress)
                    rp.save()
                    rp.allProgress.add(progress)
                    rc.allJourneys.add(rp)
                    rc.currentJourney = rp
                    rc.save()                    
                else:
                    progress = Progress(userID=progress.userID,
                                        stageID=progress.stageID.nextStage)
                    progress.save()
                
                    rp.allProgress.add(progress)
                    rp.progress = progress

            rp.distance = rp.distance + distance
            rp.save()
            rc.save()
            progress.totalDistance = progress.totalDistance + distance
            progress.totalTime = progress.totalTime + timeIncrement
            progress.save()
            
            session.save()

            payload['distance'] = session.distance
            payload['sessionTime'] = session.totalTime
            payload['distanceRemain'] = progress.stageID.distance - progress.totalDistance
            payload['stageLength'] = progress.stageID.distance
            payload['routeDistanceRemain'] = rc.routeID.length - rp.distance
            payload['routeLength'] = rc.routeID.length
            payload['currentStage'] = rp.progress.stageID.id
            payload['stageImage'] = rp.progress.stageID.image
            payload['id'] = session.pk
            payload['totalTime'] = rc.currentJourney.time
            payload['stagesCompleted'] = session.stagesCompleted

            return HttpResponse(json.dumps(payload), content_type="application/json",
                                status=202)
        else:
            return HttpResponse("Bad Request", status=400)
        
    return HttpResponse('Unauthorized method', status=401)

        
