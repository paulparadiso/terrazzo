from django.shortcuts import render
from django.http import HttpResponse
import json

from .models import MQTTUser

from .mqtt import send_mqtt

def topics(request):
    print(request.user)
    user_topics = MQTTUser.objects.filter(user=request.user)[0]
    topics = user_topics.topics.all()
    for topic in topics:
        print(topic.name)
    return render(request, "topics.html", {'topics':topics})

def run(request):
    params = json.loads(request.body)
    print(params)
    send_mqtt(params['broker']['url'], params['topic'], params['message'])
    response_data = {}
    response_data['success'] = True
    return HttpResponse(json.dumps(response_data), content_type="application/json")