from django.conf.urls import url
from elections import views

urlpatterns = [
    url(r'^general_information/$', views.general_information_list),
    url(r'^general_information/(?P<pk>[0-9]+)/$', views.general_information_detail),
]