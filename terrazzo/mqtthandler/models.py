from django.db import models
from django.contrib.auth.models import User


class MQTTBroker(models.Model):

    name = models.CharField(max_length=128)
    url = models.CharField(max_length=128)

    @classmethod
    def get_default_pk(cls):
        broker, created = cls.objects.get_or_create(
            name = "localhost",
            url = "localhost:1883"
        )
        return broker.pk
    
    def __str__(self):
        return self.name

class MQTTTopic(models.Model):

    VALUE_TYPE_CHOICES = [
        ("fixed", "Fixed"),
        ("str", "String"),
        ("number", "Number")
    ]

    name = models.CharField(max_length=30)
    path = models.CharField(max_length=128)
    broker = models.ForeignKey(MQTTBroker, on_delete=models.CASCADE, default=MQTTBroker.get_default_pk)
    message = models.CharField(max_length=250, null=True, blank=True)
    editable = models.BooleanField(default=False)
    range = models.BooleanField(default=False)
    min = models.FloatField(null=True, blank=True)
    max = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class MQTTPageConfig(models.Model):

    name = models.CharField(max_length=250)
    topics = models.ManyToManyField(MQTTTopic)

    def __str__(self):
        return self.name
    
class MQTTUser(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    topics = models.ManyToManyField(MQTTTopic)

    def __str__(self):
        return self.user.username