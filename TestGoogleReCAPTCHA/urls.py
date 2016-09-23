"""TestGoogleReCAPTCHA URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from TestGoogleReCAPTCHA.views import hello_world1,hello_world2,hello_world3,hello_world4

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello1/$', hello_world1),
    url(r'^hello2/$', hello_world2),
    url(r'^hello3/$', hello_world3),
    url(r'^hello4/$', hello_world4),
]
