from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.decorators.csrf import csrf_exempt
from . import views

urlpatterns = [
    url(r'^profile/$', views.ProfileView.as_view(), name='profile'),
    url(r'^details/$', views.AddDetails.as_view(), name='add_details'),
    url(r'^model/$',views.ModelView.as_view()),
    url(r'api/profile', views.ProfileApi.as_view(), name='api_profile'),
    # url(r'^test/',views.ProfileApi.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json'])