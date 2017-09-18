from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^details/$', views.add_details, name='add_details'),
    url(r'api/profile', views.profile_api, name='api_profile')
]
