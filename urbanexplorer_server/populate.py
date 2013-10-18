import os
import sys

def populate():
    user = addUser("TEST")
    achievement = addAchievement("First!", "First place!", "G", "You did well")
    addUserAchievement(user, achievement)

    mission = addMission("Mission A", "This is the description for Mission A")
    
    stageA = addStage("Stage A", 100)
    stageB = addStage("Stage B", 150)
    linkStages(stageA, stageB)

    routeA = addRoute("Route A", mission, stageA, stageB)

    stageC = addStage("Stage C", 100)
    stageD = addStage("Stage D", 300)
    linkStages(stageC, stageD)

    stageE = addStage("Stage E", 45)
    linkStages(stageC, stageD)
    
    routeB = addRoute("Route B", mission, stageC, stageE)

    connectRoutes(routeA, True, routeB, True)
########

def addUser(name):
    user = UserProfile.objects.get_or_create(user=User.objects.create_user(name),
                                             deviceID=name)[0]
    return user.user

def addAchievement(name, description, value, criteria):
    achievement = Achievement.objects.get_or_create(name=name,
                                                    description=description,
                                                    value=value,
                                                    criteria=criteria)[0]
    return achievement

def addUserAchievement(user, achievement):
    userAchievement = UserAchievement.objects.get_or_create(userID=user,
                                                            achievementID=achievement)[0]
    return userAchievement

def addMission(name, description):
    mission = Mission.objects.get_or_create(name=name,
                                            description=description)[0]
    return mission

def addRoute(name, mission, startStage, endStage, startConnections=None, endConnections=None):
    route = Route.objects.get_or_create(name=name,
                                        mission=mission,
                                        startStage=startStage,
                                        endStage=endStage)[0]
    return route

def addStage(name, distance, nextStage=None, previousStage=None):
    stage = Stage.objects.get_or_create(name=name,
                                        distance=distance,
                                        nextStage=nextStage,
                                        previousStage=previousStage)[0]
    return stage

def linkStages(stageA, stageB):
    objA = Stage.objects.filter(pk=stageA.pk).update(nextStage=stageB)
    objB = Stage.objects.filter(pk=stageB.pk).update(previousStage=stageA)

def connectRoutes(routeA, routeAHead, routeB, routeBHead):
    if (routeAHead and routeBHead):
        print Route.objects.filter(pk=routeA.pk)[0]
        Route.objects.filter(pk=routeA.pk)[0].startConnections.add(routeB)
        Route.objects.filter(pk=routeB.pk)[0].startConnections.add(routeA)

if __name__ == '__main__':
    print "Populating"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanexplorer_server.settings')
    from django.contrib.auth.models import User
    from api.models import UserProfile, Achievement, UserAchievement, Mission, Route, Stage
    populate()
