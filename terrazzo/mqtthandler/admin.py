from django.contrib import admin
from .models import MQTTBroker, MQTTTopic, MQTTPageConfig, MQTTUser

class UserTopicListAdmin(admin.ModelAdmin):

    filter_horizontal = ('topics',)


admin.site.register(MQTTBroker)
admin.site.register(MQTTTopic)
admin.site.register(MQTTPageConfig)
admin.site.register(MQTTUser, UserTopicListAdmin)