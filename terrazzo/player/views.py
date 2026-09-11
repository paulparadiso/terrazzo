from django.shortcuts import render
from django.db import OperationalError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlayerSerializer, VideoSerializer, SyncGroupSerializer
from .models import Player, SyncGroup

@api_view(['POST'])
def create_player_view(request):
    name = request.data.get('name')
    try:
        instance = Player.objects.get(name=name)
        serializer = PlayerSerializer(instance, data=request.data, partial=True)
    except Player.DoesNotExist:
        serializer = PlayerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_video_view(request):
    serializer = VideoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_syncgroup_view(request, name):
    try:
        syncgroup = SyncGroup.objects.get(name=name)
        serializer = SyncGroupSerializer(syncgroup)
        return Response(serializer.data)
    except:
        return Response({"status": "error"})

