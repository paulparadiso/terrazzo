import paho.mqtt.client as mqtt

def send_mqtt(broker, topic, message):
    tokens = broker.split(':')
    mqttc = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    mqttc.connect(tokens[0], int(tokens[1]))
    mqttc.publish(topic, message)
    mqttc.disconnect()