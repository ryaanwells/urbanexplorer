import os
import sys

def purge():
    purgeUsers()
    purgeUserProfile()
    purgeAchievement()
    purgeUserAchievement()
    purgeMission()
    purgePlace()
    purgeRoute()
    purgeStage()
    purgeProgress()
    purgeRoutesCompleted()
    purgeSession()
########

def purgeUsers():
    User.objects.exclude(is_superuser=True).delete()

def purgeUserProfile():
    UserProfile.objects.all().delete()

def purgeAchievement():
    Achievement.objects.all().delete()

def purgeUserAchievement():
    UserAchievement.objects.all().delete()

def purgeMission():
    Mission.objects.all().delete()

def purgePlace():
    Place.objects.all().delete()

def purgeRoute():
    Route.objects.all().delete()

def purgeStage():
    Stage.objects.all().delete()

def purgeProgress():
    Progress.objects.all().delete()

def purgeRoutesCompleted():
    RoutesCompleted.objects.all().delete()

def purgeSession():
    Session.objects.all().delete()

if __name__ == '__main__':
    print "Purging..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanexplorer_server.settings')
    from django.contrib.auth.models import User
    from api.models import UserProfile, Achievement, UserAchievement, Mission, Place, Route, Stage, Progress, RoutesCompleted, Session
    purge()
    print "Done"
