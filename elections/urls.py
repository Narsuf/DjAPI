from django.conf.urls import url
from elections import views

urlpatterns = [
    url(r'^elections$', views.elections_list),
    url(r'^elections/(?P<id>[0-9]+)$', views.election_detail),
    url(r'^parties$', views.parties_list),
    url(r'^parties/(?P<id>[0-9]+)$', views.party_detail),
    url(r'^results$', views.results_list),
    url(r'^results/(?P<id>[0-9]+)$', views.results_detail)
]
