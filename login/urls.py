from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login, name = 'login'),
    path('signup',views.signup, name = 'signup'),
    path('logout',views.logout, name = 'logout'),
    path('profile',views.profile, name = 'profile'),
    path('changeprofile',views.user_change, name = 'change_profile'),
    path('changepass',views.pass_change, name = 'pass_change'),
    path('changephoto',views.add_pro_pic, name = 'add_pro_pic'),
    path('changepic',views.change_pro_pic, name = 'change_pro_pic'),
]