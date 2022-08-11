"""meteorites URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from shop.views import main, product
from users.views import profile, user_authorization, user_exit


urlpatterns = [
    path('', main, name='main'),
    path('admin/', admin.site.urls),
    path('logout/', user_exit, name='logout'),
    path('profile/', profile, name='profile'),
    path('product/<slug:slug>', product, name='product'),
    path('authorization/', user_authorization, name='authorization'),
]
