from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^lastupdated/$', views.LastUpdatedView.as_view()),
    url(r'^$', views.PlaceList.as_view()),
    #url(r'^near/$', views.PlaceNear.as_view()),
    #url(r'^(?P<pk>[0-9]+)/$', views.PlaceDetail.as_view())
]
