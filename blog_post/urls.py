from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('my_blog',views.mybloglist, name = 'my_blog_list'),
]