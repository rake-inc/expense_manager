from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signup/$',views.UserSignup.as_view(),name='signup'),
    url(r'^login/$',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/$',views.AuthLogout.as_view(),name='logout'),
    url(r'^$',views.Home.as_view(),name='root_home'),
    url(r'^accounts/',include('accounts.urls'))
]
