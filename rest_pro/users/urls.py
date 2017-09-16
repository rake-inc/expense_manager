from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^signup/',views.user_signup,name='signup'),
    url(r'^login/',auth_views.login,{'template_name':'login.html'},name='login'),
    url(r'^logout/',views.auth_logout,name='logout'),
    url(r'^$',views.home,name='root_home'),
    url(r'^accounts/',include('accounts.urls'))
]
