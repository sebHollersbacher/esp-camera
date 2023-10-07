
import time
import paho.mqtt.client as paho
import paho.mqtt.publish as publish
import threading


def on_message(mosq, obj, msg):
  print(msg.topic, msg.qos, msg.payload)
  #mosq.publish('pong', 'ack', 0)
  
def on_publish(mosq, obj, mid):
  pass

class Sub():

  def __init__(self):
    self._thread=threading.Thread(name='sub',target=self.run)
    self._thread.deamon = True
    self._thread_active = True
    
    self.client = paho.Client()
    self.client.on_message = on_message
    self.client.on_publish = on_publish
    self.client.connect("192.168.178.48", 1883, 60)
    self.client.subscribe("testTopic")
    
    self._thread.start()
    

  def run(self):
    print("sub thread started")
    while self.client.loop() == 0 and self._thread_active:
        pass
      
  def stop(self):
    print("stopping sub")
    self._thread_active = False



class Pub():
  def __init__(self):
    self._thread=threading.Thread(name='sub',target=self.run)
    self._thread.deamon = True
    self._thread_active = True

    self.host = "localhost"
    
    self._thread.start()
    

  def run(self):
    print("pub thread started")
    while self._thread_active:
      publish.single(topic="testTopic", payload="just do it", hostname=self.host)
      time.sleep(1)
  
      
  def stop(self):
    print("stopping sub")
    self._thread_active = False




if __name__ == '__main__':
  try:
    #sub = Sub()
    pub = Pub()
    while True:
      pass
    
  except KeyboardInterrupt:     
      #sub.stop()   
      pub.stop()
      time.sleep(1)
    