"""
URL configuration for network_breakdown project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    #主要界面url
    path('',views.index,name = 'index'),

    #论坛界面url
    path('forum/',views.forums,name = 'forum'),
    path('forum/<int:blog_id>/',views.blog,name = 'forum'),
    path('forum/new_blog/',views.new_blog,name = 'new_blog'),

    #资料界面url
    path('topic/',views.topic,name = 'topic'),
    path('entry/<int:entry_id>',views.entry,name = 'entry'),
    path('data/<int:data_id>',views.data,name = 'data'),

    #用户组界面url
    path('users/',include('django.contrib.auth.urls'),name = 'users'),
    path('users/register/',views.register,name = 'register'),

    #关于我们界面url
    path('about/',views.about,name = 'about'),

]
