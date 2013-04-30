from django.conf.urls import patterns, include, url
from .views import getImage, ImageListView

urlpatterns = patterns('',
    url(r'^get$', getImage, name='get-images'),
    url(r'^$', ImageListView.as_view(), name='home'),
)