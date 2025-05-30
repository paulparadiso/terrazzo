# Generated by Django 5.2 on 2025-05-30 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mqtthandler', '0005_mqttmessage_alter_mqtttopic_type_mqttmessagefixed_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mqttmessagefixed',
            name='mqttmessage_ptr',
        ),
        migrations.AddField(
            model_name='mqtttopic',
            name='editable',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='mqtttopic',
            name='max',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mqtttopic',
            name='message',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='mqtttopic',
            name='min',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='mqtttopic',
            name='range',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='MQTTMessageNumber',
        ),
        migrations.DeleteModel(
            name='MQTTMessage',
        ),
        migrations.DeleteModel(
            name='MQTTMessageFixed',
        ),
    ]
