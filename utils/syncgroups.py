import requests
import paho.mqtt.client as mqtt
from paho.mqtt.enums import CallbackAPIVersion
import redis
import time

SYNCGROUP_TOPIC = '/museum/players/syncgroup/+'

redis_db = redis.Redis(
    host='localhost',
    port=6379,
    db=0,
    password=None,
    decode_responses=True
)

broker = redis_db.get('mqtt_broker')
server_url = redis_db.get('server_url')

def on_connect(client, userdata, flags, reason_code, properties):
    print(f"connected: {reason_code}")
    client.subscribe(SYNCGROUP_TOPIC)
    print(f"Subscribed to: {SYNCGROUP_TOPIC}.")

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    syncgroup = msg.topic.split('/')[-1]
    print(f'Received {payload} for {syncgroup}')
    r = requests.get(f'{server_url}/syncgroup/{syncgroup}')
    data = r.json()
    print(data)
    if 'players' in data.keys():
        for player in data['players']:
            print(f'Publishing to {player}')
            topic = f'/museum/players/{player}'
            client.publish(topic, payload=payload, qos=1, retain=False)
            #msg_info.wait_for_publish()
            print(f'Sent {payload} to {topic}')

client = mqtt.Client(CallbackAPIVersion.VERSION2)
client.on_connect = on_connect
client.on_message = on_message

BROKER_ADDRESS = redis_db.get('mqtt_broker')
PORT = 1883
KEEP_ALIVE = 60

client.connect(BROKER_ADDRESS, PORT, KEEP_ALIVE)

print('Waiting for messages.')
client.loop_forever()
