import os
import sys

def purge():
    purgeUsers()
    purgeUserProfile()

def purgeUsers():
    User.objects.exclude(is_superuser=True).delete()

def purgeUserProfile():
    UserProfile.objects.all().delete()

if __name__ == '__main__':
    print "Purging..."
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'urbanexplorer_server.settings')
    from django.contrib.auth.models import User
    from api.models import UserProfile
    purge()
    print "Done"
