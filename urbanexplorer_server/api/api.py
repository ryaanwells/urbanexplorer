from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie import fields
from django.contrib.auth.models import User
from models import UserProfile, Session, Progress, Stage

class UserResource(ModelResource):
    class Meta:
        queryset = User.objects.all()
        resource_name = 'user'
        authorization = Authorization()
        allowed_methods = ['get', 'post']

class UserProfileResource(ModelResource):
    user = fields.ForeignKey(UserResource, 'user')
    class Meta:
        queryset = UserProfile.objects.all()
        resource_name = 'userprofile'
        authorization = Authorization()
        fields = ['deviceID', 'resourceURI']
        allowed_methods = ['get']
        filtering = {
            'deviceID': ALL
        }

class StageResource(ModelResource):
    class Meta:
        queryset = Stage.objects.all()
        resource_name = 'stage'
        authorization = Authorization()
        allowed_methods = ['get']

class ProgressResource(ModelResource):
    
    userID = fields.ForeignKey(UserProfileResource, 'userID')
    stageID = fields.ForeginKey(StageResource, 'stageID')

    class Meta:
        queryset = Progress.objects.all()
        resource_name = 'progress'
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'patch']
        filtering = {
            'deviceID': ALL,
            'userID': ALL
        }
    

class SessionResource(ModelResource):
    userID = fields.ForeignKey(UserProfileResource, 'userID')
    currentProgress = fields.ForeignKey(ProgressResource, 'currentProgress')
    allProgress = fields.ManyToManyField(ProgressResource, 'allProgress')

    class Meta:
        queryset = Session.objects.all()
        resource_name = 'session'
        authorization = Authorization()
        allowed_methods = ['get', 'post', 'patch']
