from tastypie.resources import ModelResource, ALL
from tastypie.authorization import Authorization
from tastypie import fields
from django.contrib.auth.models import User
from models import UserProfile

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
