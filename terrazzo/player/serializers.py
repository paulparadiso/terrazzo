from rest_framework import serializers
from django.utils import timezone
from .models import Player, Video, SyncGroup

class PlayerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Player
        fields = '__all__'

    #def update(self, instance, validated_data):
    #    instance.modified_at = timezone.now()

class VideoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Video
        fields = '__all__'

class SyncGroupSerializer(serializers.ModelSerializer):
    players = serializers.StringRelatedField(many=True, read_only=True)

    class Meta:
        model = SyncGroup
        fields = '__all__'