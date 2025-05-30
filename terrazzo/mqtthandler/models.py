from django.db import models

# Create your models here.

class MQTTBroker(models.Model):

    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)

class MQTTTopic(models.Model):

    VALUE_TYPE_CHOICES = [
        ("str", "String"),
        ("int", "Integer"),
        ("float", "Float")
    ]

    name = models.CharField(max_length=30)
    path = models.CharField(max_length=128)
    type = models.CharField(max_length=10, choices=VALUE_TYPE_CHOICES)
    broker = models.ForiegnKey(MQTTBroker, on_delete=models.CASCADE)

