from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from api_v0.views import BeingList, BeingDetail

urlpatterns = [
    url(r'^biengs/$', BeingList.as_view(), name="being-list"),
    url(r'^bieng/(?P<pk>[0-9]+)/$', BeingDetail.as_view(), name="being-detail"),
]

urlpatterns = format_suffix_patterns(urlpatterns)