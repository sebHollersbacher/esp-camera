#include <Arduino.h>
#include <WiFi.h>
#include <PubSubClient.h>

int relay = 2;

const char* mqtt_server = "192.168.0.27"; // Add your IP here (IP of device where you installed Home Assistant)
WiFiClient espClient;
PubSubClient client(espClient);

void callback(char* topic, byte* payload, unsigned int length) {

  Serial.print("Message arrived in topic: ");
  Serial.println(topic);

  Serial.print("Message: ");

  String message;
  for (int i = 0; i < length; i++) {
    message = message + (char)payload[i];
  }
   Serial.print(message);
  if(message == "0") {digitalWrite(relay,LOW);}
  if(message == "1") {digitalWrite(relay,HIGH);}

  Serial.println();
}

void setup() {
  pinMode(relay,OUTPUT);
  digitalWrite(relay, LOW);

  Serial.begin(74880);
  Serial.println("Readings will apear here.");

  WiFi.begin("SSID","password"); // Add your Wi-Fi name and password here
  Serial.print("Connecting");
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
    Serial.print(".");
  }
  Serial.println();
  Serial.print("Connected, IP address: ");
  Serial.println(WiFi.localIP());

  digitalWrite(relay, HIGH);

  client.setServer(mqtt_server,1883);
  client.setCallback(callback);

  if(client.connect("Light")){
    Serial.println("Light - MQTT - OK");
    client.subscribe("testTopic");
  }else{
    Serial.println("Light - MQTT - ERROR");
  }
}

void loop() {
  client.loop();
}
