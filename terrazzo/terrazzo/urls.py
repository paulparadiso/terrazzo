"""
URL configuration for terrazzo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from mqtthandler import views as mqtt_views
from inventory import views as inventory_views
from player.views import create_player_view, create_video_view

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('mqtt', mqtt_views.topics, name='topics'),
    path('mqtt/run', mqtt_views.run, name='run'),
    path('inventory/categories/add', inventory_views.add_category, name='inventory_category_add'),
    path('inventory/fields/add', inventory_views.add_fields, name='inventory_fields_add'),
    path('inventory/category/<str:category_name>', inventory_views.category, name='inventory_view_category'),
    path('players', create_player_view, name='add-player'),
    path('videos', create_video_view, name='add-video')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
