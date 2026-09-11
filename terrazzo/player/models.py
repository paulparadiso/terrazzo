from django.db import models

class Player(models.Model):

    name = models.CharField(max_length=128, unique=True)
    ip_address = models.CharField(max_length=32)
    mac_address = models.CharField(max_length=128)
    version = models.CharField(max_length=128)

    current_config = models.ForeignKey(
        'PlayerConfig', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True,
        related_name='current_config'    
    )

    def __str__(self):
        return self.name

class Video(models.Model):

    name = models.CharField(max_length=128)
    path = models.CharField(max_length=128)
    duration = models.FloatField(null=True, blank=True)
    frame_rate = models.FloatField(null=True, blank=True)
    media_type = models.CharField(max_length=128, null=True, blank=True)
    width = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)

    player = models.ForeignKey(
        'Player', 
        to_field='name',
        on_delete=models.CASCADE, 
        related_name='videos'
    )

    def __str__(self):
        return self.name

class PlayerConfig(models.Model):

    name = models.CharField(max_length=128)
    screen1 = models.OneToOneField('Video', on_delete=models.CASCADE, related_name='video1')
    screen2 = models.OneToOneField('Video', on_delete=models.CASCADE, related_name='video2') 

    player = models.ForeignKey(
        'Player', 
        on_delete=models.CASCADE, 
        related_name='configs'
    )

    def __str__(self):
        return self.name
