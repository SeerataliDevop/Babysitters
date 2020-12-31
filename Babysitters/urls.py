"""Babysitters URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.urls import path

from Babysitters import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login', views.login_view, name="login"),
    path('signup', views.signup_view, name="signup"),
    path('search', views.search, name="search"),
    path('', views.home, name="home"),
    path('contact', views.contact, name="contact"),
    path('logout', views.log_out, name="logout"),
    path('about', views.about, name="about"),
    path('available', views.available, name="available"),
    path('available_multan', views.available_multan, name="available_multan"),
    path('available_islamabad', views.available_islamabad, name="available_islamabad"),
    path('available_gujranwala', views.available_gujranwala, name="available_gujranwala"),
    path('available_karachi', views.available_karachi, name="available_karachi"),
    path('available_sialkot', views.available_sialkot, name="available_sialkot"),
    path('available_peshawar', views.available_peshawar, name="available_peshawar"),
    path('available_gujrat', views.available_gujrat, name="available_gujrat"),
    path('packages', views.packages, name="packages"),
    path('register', views.register, name="register"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
