from django.conf.urls import url
from elections import views

urlpatterns = [
    url(r'^elections/$', views.elections_list),
    url(r'^election/(?P<year>[0-9]{4})/(?P<place>\w+)/(?P<chamber_name>\w+)/$', views.election_detail),
    url(r'^parties/$', views.parties_list),
    url(r'^party/(?P<name>\w+)/$', views.party_detail),
    url(r'^results/(?P<year>[0-9]{4})/(?P<place>\w+)/(?P<chamber_name>\w+)/$', views.results_list),
    url(r'^results/(?P<year>[0-9]{4})/(?P<place>\w+)/(?P<chamber_name>\w+)/(?P<name>\w+)/$', views.results_detail)
]
