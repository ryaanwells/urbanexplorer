# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from api import UserProfileResource
from models import UserProfile, Session, Progress, Stage, Route, RoutesCompleted
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
        for s in route.stages.all():
            print s
            prog = Progress.objects.filter(userID=userID, stageID=s)
            if not prog or not prog[0].completed:
                startStage = s
                break
        if not startStage:
            return HttpResponse("Route completed", status=401)
        
        progress = Progress.objects.get_or_create(userID=userID, stageID=startStage)[0]
        session = Session.objects.create(userID=userID, currentProgress=progress, route=route,
                                         lastLat=float(body['lat']), lastLon=float(body['lon']),
                                         lastTime=body['timestamp'])
        session.allProgress.add(progress)
        session.save()
        
        response = {}
        response['id'] = session.pk
        
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

            session.distance = session.distance + distance
            session.lastLat = body['lat']
            session.lastLon = body['lon']
            session.totalTime = session.totalTime + timeIncrement
            session.lastTime = body['timestamp']

            session.userID.totalTime = session.userID.totalTime + timeIncrement
            session.userID.totalDistance = session.userID.totalDistance + distance
            session.userID.save()
            
            progress = session.currentProgress
            stage =  progress.stageID

            rc = RoutesCompleted.objects.get_or_create(routeID=session.route, userID=session.userID)[0]
            rc.totalTime = rc.totalTime + timeIncrement

            if progress is not None:
                progress.totalTime = progress.totalTime + timeIncrement

            while progress is not None and distance > 0:
                if progress.totalDistance + distance >= stage.distance:
                    difference = progress.totalDistance + distance - stage.distance
                    progress.totalDistance = stage.distance
                    progress.completed = True
                    progress.save()
                    
                    if stage.nextStage is not None:
                        progress = Progress.objects.get_or_create(userID=session.userID,
                                                                  stageID=stage.nextStage)[0]
                        progress.totalDistance = difference
                        progress.save()
                        session.currentProgress = progress
                        session.allProgress.add(progress)
                        stage = stage.nextStage
                    else:
                        stage = None
                        progress = None
                        session.excessDistance = distance
                        distance = 0
                        rc.completed = True
                        rc.completionDate = datetime.datetime.now()
                else:
                    progress.totalDistance = progress.totalDistance + distance
                    distance = 0
            
            session.save()
            rc.save()

            payload = {}
            payload['distance'] = session.distance
            payload['totalTime'] = session.totalTime
            payload['excessDistance'] = session.excessDistance
            remain = 0;
            if progress and stage:
                remain = stage.distance - progress.totalDistance
                
            payload['distanceRemain'] = remain

            return HttpResponse(json.dumps(payload), content_type="application/json",
                                status=202)
        else:
            return HttpResponse("Bad Request", status=400)
        
    return HttpResponse('Unauthorized method', status=401)

        
