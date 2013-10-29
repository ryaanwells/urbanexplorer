import os
import sys

def populate():
    user = addUser("Ryan")
    #achievement = addAchievement("First!", "First place!", "G", "You did well")
    #addUserAchievement(user, achievement)

    arranMission = addMission("Isle of Arran", "Run around the beautiful countryside of Arran!")
    
    brodick = addPlace("Brodick", arranMission)
    lamlash = addPlace("Lamlash", arranMission)
    
    brodickTownStage = addStage("Brodick Town", 1500)
    strathwhillanWood = addStage("Strathwhillan Wood", 3500)
    lamlashBay = addStage("Lamlash Bay", 1000)
    linkStages(brodickTownStage, strathwhillanWood)
    linkStages(strathwhillanWood, lamlashBay)

    addRoute("Brodick to Lamlash", arranMission,
             brodickTownStage, lamlashBay,
             brodick, lamlash)

    whittingBay = addPlace("Whitting Bay", arranMission)
    cuddyStage = addStage("The Cuddy", 1000)
    whiteField = addStage("Whitefield", 2000)
    kingscrossBurn = addStage("Kings Cross Burn", 1500)
    linkStages(cuddyStage, whiteField)
    linkStages(whiteField, kingscrossBurn)
    
    addRoute("Lamlash to Whiting Bay", arranMission,
             cuddyStage, kingscrossBurn,
             lamlash, whittingBay)


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

def addRoute(name, mission, startStage, endStage, startPlace, endPlace):
    route = Route.objects.get_or_create(name=name,
                                        mission=mission,
                                        startStage=startStage,
                                        endStage=endStage,
                                        startPlace=startPlace,
                                        endPlace=endPlace)[0]
    return route

def addStage(name, distance, nextStage=None, previousStage=None):
    stage = Stage.objects.get_or_create(name=name,
                                        distance=distance,
                                        nextStage=nextStage,
                                        previousStage=previousStage)[0]
    return stage

def addPlace(name, mission):
    place = Place.objects.get_or_create(name=name,
                                        mission=mission)[0]
    return place

def linkStages(stageA, stageB):
    objA = Stage.objects.filter(pk=stageA.pk).update(nextStage=stageB)
    objB = Stage.objects.filter(pk=stageB.pk).update(previousStage=stageA)


if __name__ == '__main__':
    print "Populating"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanexplorer_server.settings')
    from django.contrib.auth.models import User
    from api.models import UserProfile, Achievement, UserAchievement, Mission, Place, Route, Stage, Progress, RoutesCompleted, Session
    populate()
