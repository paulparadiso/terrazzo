from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin.helpers import ACTION_CHECKBOX_NAME
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import Player, PlayerConfig, Video, SyncGroup
from .forms import AddToSyncGroupForm

@admin.action(description="Add player to sync group.")
def add_to_syncgroup_action(modeladmin, request, queryset):
    if 'apply' in request.POST:
        form = AddToSyncGroupForm(request.POST)
        if form.is_valid():
            syncgroup = form.cleaned_data['syncgroup']
            player_ids = request.POST.getlist(ACTION_CHECKBOX_NAME)
            selected_players = Player.objects.filter(pk__in=player_ids)
            syncgroup.players.add(*selected_players)

            modeladmin.message_user(
                request,
                f"Added {selected_players.count()} players to {syncgroup}"
            )
            return None
    else:
        initial_data = {
            ACTION_CHECKBOX_NAME: request.POST.getlist(ACTION_CHECKBOX_NAME)
        }
        form = AddToSyncGroupForm(initial=initial_data)

    return render(
        request, 
        'admin/add_to_syncgroup_intermediate.html',
        context={
            'players': queryset,
            'form': form,
            'action': 'add_to_syncgroup_action',
            'opts': modeladmin.model._meta,
        }
    )

class PlayerAdmin(admin.ModelAdmin):
    list_display = ("name", "ip_address", "version")
    actions = [add_to_syncgroup_action]

    @admin.display(description='Status')
    def status_led(self, obj):
        if obj.is_online:
            # Green LED dot
            return format_html('<span style="color: #2ecc71; font-size: 1.5em;">●</span> Online')
        else:
            # Red LED dot
            return format_html('<span style="color: #e74c3c; font-size: 1.5em;">●</span> Offline')

admin.site.register(Player, PlayerAdmin)
#admin.site.register(PlayerConfig)
#admin.site.register(Video)
admin.site.register(SyncGroup)