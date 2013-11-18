# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.models import User
from api import UserProfileResource
from models import UserProfile
import json

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

