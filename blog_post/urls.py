from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = 'home'),
    path('my_blog',views.mybloglist, name = 'my_blog_list'),
    path('create_blog',views.CreateBlog.as_view(), name = 'create_blog'),
    path('blog_detail/<slug:slug>',views.blog_detail, name = 'blog_detail'),
    path('myblogs',views.MyBlog.as_view(), name = 'myblog'),
    path('editblog/<int:pk>',views.UpdateBlog.as_view(), name = 'editblog'),
]