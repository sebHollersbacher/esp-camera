import paho.mqtt.client as paho
import time
import paho.mqtt.publish as publish

def on_message(mosq, obj, msg):
    print(msg.topic, msg.qos, msg.payload)
    # mosq.publish('pong', 'ack', 0)


def on_publish(mosq, obj, mid):
    pass


def subscribe():
    client = paho.Client()
    client.on_message = on_message
    client.on_publish = on_publish
    client.connect("192.168.0.27", 1883, 60)
    client.subscribe("testTopic")

    while client.loop() == 0:
        pass

def pub():
    host = "192.168.0.27"
    while True:
        input1 = input()
        publish.single(topic="testTopic", payload=input1, hostname=host)
        time.sleep(1)


if __name__ == '__main__':
    pub()
