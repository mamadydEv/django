from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('register/' , views.user_register , name = 'user_register'),
    path('login/' , views.user_login , name = 'login'),
    path('logout/' , views.user_logout , name ='logout'),
    path('profile/' , views.profile , name = 'profile'),
    path('update/' , views.update_profile , name = 'update'),
    path('change/' , views.change_pass , name = 'change')
]