import os
import sys

def populate():
    user = addUser("TEST")
    achievement = addAchievement("First!", "First place!", "G", "You did well")
    addUserAchievement(user, achievement)

def addUser(name):
    user = UserProfile.objects.get_or_create(user=User.objects.create_user(name),
                                             deviceID=name)[0]
    return user.user

def addAchievement(name, description, value, criteria):
    achievement = Achievement.objects.get_or_create(name=name,
                                                    description=description,
                                                    value=value,
                                                    criteria=criteria)[0]
    print achievement
    return achievement

def addUserAchievement(user, achievement):
    userAchievement = UserAchievement.objects.get_or_create(userID=user,
                                                            achievementID=achievement)
    return userAchievement

if __name__ == '__main__':
    print "Populating"
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanexplorer_server.settings')
    from django.contrib.auth.models import User
    from api.models import UserProfile, Achievement, UserAchievement
    populate()
