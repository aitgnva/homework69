"""api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from webapp.views import index, add_view, subtract_view, divide_view, multiply_view, get_token_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('add/', add_view, name='add_view'),
    path('subtract/', subtract_view, name='subtract_view'),
    path('divide/', divide_view, name='divide_view'),
    path('multiply/', multiply_view, name='multiply_view'),

]
