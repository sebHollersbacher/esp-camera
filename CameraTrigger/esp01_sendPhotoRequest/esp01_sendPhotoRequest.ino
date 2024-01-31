#include <Arduino.h>
#include <ESP8266WiFi.h>
#include <PubSubClient.h>

const char* mqtt_server = "192.168.0.27";
WiFiClient espClient;
PubSubClient client(espClient);

void setup() {
  pinMode(2, INPUT);  // GPIO2 must be HIGH when restarting

  WiFi.begin("SSID","password");
  while(WiFi.status() != WL_CONNECTED){
    delay(1000);
  }

  client.setServer(mqtt_server,1883);
  client.connect("ESP_1");
}

void loop() {
  if(!digitalRead(2)) {
    client.publish("esp_cam_0", "1");
    delay(2000);
  }
  delay(200);
}
