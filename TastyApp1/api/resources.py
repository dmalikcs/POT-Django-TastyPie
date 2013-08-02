from tastypie.resources import ModelResource
from TastyApp1.models import A1M1_information,A1M2_extainfo
from tastypie.authentication import Authentication,ApiKeyAuthentication
from tastypie.authentication import BasicAuthentication
from tastypie.authorization import DjangoAuthorization,Authorization,ReadOnlyAuthorization
from tastypie.serializers import Serializer
from tastypie.throttle import CacheDBThrottle

from tastypie import fields


class UserResource(ModelResource):
    def dehydrate_Lname(self,bundle):
        return bundle.data['Lname'].upper()
    def dehydrate_Fname(self,bundle):
        return bundle.data['Fname']
    def dehydrate(self,bundle):
        bundle.data['REMOTE_ADDR']=bundle.request.META['REMOTE_ADDR']
        return bundle 
    def hydrate_Lname(self,bundle):
        bundle.data['Lname']=bundle.data['Lname'].lower()
        print bundle.data['Lname']
        return bundle
    def hydrate(self,bundle):
        print  " Hydrate %s" % bundle
        print "Anything need to update here "
        return bundle 

    class Meta:
        queryset=A1M1_information.objects.all()
        resource_name='user'
        #fields=['Lname','Fname','email']
        api_name="Deepak"
        max_limit=2
        allowed_methods=['get','post']
        #authentication=ApiKeyAuthentication()
        #authorization=ReadOnlyAuthorization()
        throttle=CacheDBThrottle()


class UserExtaResource(ModelResource):
    users=fields.ForeignKey(UserResource,'users_fk')
    class Meta:
        queryset=A1M2_extainfo.objects.all()
        resource_name='extra'
