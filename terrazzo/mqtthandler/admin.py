from django.contrib import admin
from .models import MQTTBroker, MQTTTopic

# Register your models here.

admin.site.register(MQTTBroker)
admin.site.register(MQTTTopic)