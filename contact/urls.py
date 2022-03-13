"""contact URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import include
from django.urls import path
from app import views
from django.contrib.auth.views import LoginView,LogoutView



urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.adminsignup_view),
    path('adminsignup', views.adminsignup_view),

    path('adminlogin', LoginView.as_view(template_name='app/adminlogin.html')),

    path('logout', LogoutView.as_view(template_name='app/logout.html')),

    path('afterlogin', views.afterlogin_view),
    path('afterlogin/logout', LogoutView.as_view(template_name='app/logout.html')),
    
    path('addcontact/', views.addcontact_view),
    path('addcontact/logout', LogoutView.as_view(template_name='app/logout.html')),

    path('viewcontact/', views.viewcontact_view),
    path('viewcontact/logout', LogoutView.as_view(template_name='app/logout.html')),

]
