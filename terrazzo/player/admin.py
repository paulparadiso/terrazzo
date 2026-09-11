from django.contrib import admin
from .models import Player, PlayerConfig, Video

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "ip_address", "version")

admin.site.register(Player, PlayerAdmin)
admin.site.register(PlayerConfig)
admin.site.register(Video)
