from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.authorization import Authorization
from tastypie import fields
from django.contrib.auth.models import User
from models import UserProfile, Session, Progress, Stage, Mission, Place, Route

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
    nextStage = fields.ToOneField('api.api.StageResource', 'nextStage', null=True)
    previousStage = fields.ToOneField('api.api.StageResource', 'previousStage', null=True)

    class Meta:
        queryset = Stage.objects.all()
        resource_name = 'stage'
        authorization = Authorization()
        allowed_methods = ['get']
        filtering = {
            "name": ALL,
            "distance": ALL,
            "nextStage": ALL_WITH_RELATIONS,
            "previousStage": ALL_WITH_RELATIONS,
            "resource_uri": ALL,
            "id": ALL
        }

class MissionResource(ModelResource):
    class Meta:
        queryset = Mission.objects.all()
        resource_name= 'mission'
        authorization = Authorization()
        allowed_methods = ['get']
        filtering = {
            'name': ALL
        }

class PlaceResource(ModelResource):
    mission = fields.ForeignKey(MissionResource, 'mission')
    
    class Meta:
        queryset = Place.objects.all()
        resource_name= 'place'
        authorization = Authorization()
        allowed_methods = ['get']
        filtering = {
            'name': ALL,
            'mission': ALL
        }

class RouteResource(ModelResource):
    mission = fields.ForeignKey(MissionResource, 'mission')
    startPlace = fields.ForeignKey(PlaceResource, 'startPlace')
    endPlace = fields.ForeignKey(PlaceResource, 'endPlace')
    startStage = fields.ForeignKey(StageResource, 'startStage')
    endStage = fields.ForeignKey(StageResource, 'endStage')
    stages = fields.ToManyField(StageResource, 'stages')
    
    class Meta:
        queryset = Route.objects.all()
        resource_name= 'route'
        authorization = Authorization()
        allowed_methods = ['get']
        filtering = {
            'name': ALL,
            'mission': ALL,
            'startPlace': ALL_WITH_RELATIONS,
            'endPlace': ALL_WITH_RELATIONS,
            'startStage': ALL_WITH_RELATIONS,
            'endStage': ALL_WITH_RELATIONS,
            'stages': ALL_WITH_RELATIONS
        }

class ProgressResource(ModelResource):
    
    userID = fields.ForeignKey(UserProfileResource, 'userID')
    stageID = fields.ForeignKey(StageResource, 'stageID')

    class Meta:
        queryset = Progress.objects.all()
        resource_name = 'progress'
        authorization = Authorization()
        allowed_methods = ['get']
        filtering = {
            'stageID': ALL_WITH_RELATIONS,
            'userID': ALL_WITH_RELATIONS,
            'completed': ALL
        }
        always_return_data = True

class SessionResource(ModelResource):
    userID = fields.ForeignKey(UserProfileResource, 'userID')
    currentProgress = fields.ForeignKey(ProgressResource, 'currentProgress')
    allProgress = fields.ToManyField(ProgressResource, 'allProgress')

    class Meta:
        queryset = Session.objects.all()
        resource_name = 'session'
        authorization = Authorization()
        allowed_methods = ['get']
        always_return_data = True
