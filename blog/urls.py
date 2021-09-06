

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog_post.urls')),
    path('accounts/',include('login.urls')),
]
