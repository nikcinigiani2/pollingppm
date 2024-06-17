"""
URL configuration for PollingApp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path, include
from polls_app.Views import *
from django.contrib.auth.views import LoginView


urlpatterns = [
    path('polls/', PollList.as_view(), name='poll_list'),
    path('home/', home, name='home'),
    path('home/<int:poll_id>/', home, name='home'),
    path('', login_view, name='Login'),
    path('Login/', login_view , name='Login'),
    path('polls/<int:pk>/', PollDetail.as_view(), name='poll_detail'),
    path('polls/<int:poll_id>/choices/', ChoiceCreate.as_view(), name='choice_create'),
    path('polls/<int:pk>/choices/<int:choice_id>/vote/', Vote.as_view(), name='vote'),
    path('admin/', admin.site.urls),
    path('polls/create/', CreatePoll, name='CreatePoll'),
    path('api-auth/', include('rest_framework.urls')),
    path('register/', Register, name='register'),
    path('logout/', Logout, name='logout'),
    path('delete_poll/<int:pk>/', delete_Poll, name='delete_Poll'),




]



