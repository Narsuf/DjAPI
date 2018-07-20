from django.conf.urls import url
from elections import views

urlpatterns = [
    url(r'^general_information/$', views.general_information_list),
    url(r'^general_information/(?P<year>[0-9]{4})/(?P<place>\w+)/(?P<chamber_name>\w+)/$', views.general_information_detail),
    url(r'^party/$', views.party_list),
    url(r'^party/(?P<year>[0-9]{4})/(?P<place>\w+)/(?P<chamber_name>\w+)/(?P<color>\w+)/$', views.party_detail),
]
