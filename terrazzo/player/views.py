from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import PlayerSerializer, VideoSerializer

@api_view(['POST'])
def create_player_view(request):
    serializer = PlayerSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(seriaizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def create_video_view(request):
    serializer = VideoSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




