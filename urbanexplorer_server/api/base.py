from tastypie.resources import ModelResource

class uMeta(object):
    include_resource_uri = True
    always_return_data = True
    allowed_methods = ['get', 'post', 'patch']

