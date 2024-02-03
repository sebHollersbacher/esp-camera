#include "soc/soc.h"
#include "soc/rtc_cntl_reg.h"
#include "esp_camera.h"
#include "HTTPClient.h"
#include <PubSubClient.h>
#include <WiFiManager.h>  

#define SERVER_IP "192.168.178.48"

const char* mqtt_server = SERVER_IP;
const char *post_url = "http://" SERVER_IP ":8000/upload-image";

void callback(char* topic, byte* payload, unsigned int length);
WiFiClient espClient;
PubSubClient client(espClient);

// CAMERA_MODEL_AI_THINKER
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27

#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22

const int timerInterval = 10000;    // time between each HTTP POST image
unsigned long previousMillis = 0;   // last time image was sent

void setup() {
  WRITE_PERI_REG(RTC_CNTL_BROWN_OUT_REG, 0); 
  pinMode(4, OUTPUT);
  Serial.begin(115200);

  // Setup WiFi
  WiFiManager wifiManager;
  wifiManager.autoConnect("ESP32");

  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sscb_sda = SIOD_GPIO_NUM;
  config.pin_sscb_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;

  config.pixel_format = PIXFORMAT_JPEG;
  config.frame_size = FRAMESIZE_VGA;   // resolution UXGA
  config.jpeg_quality = 10;  //0-63 lower number means higher quality
  config.fb_count = 1;  // use 1 framebuffer as we are sending 1 image
  
  // camera init
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    delay(1000);
    ESP.restart();
  }
  
  // MQTT
  client.setServer(mqtt_server, 1883);
  client.setCallback(callback);
  startMQTT();

  Serial.println("Setup finished");
}

void callback(char* topic, byte* payload, unsigned int length) {
  Serial.print("Message in topic: ");
  Serial.println(topic);
  for (int i = 0; i < length; i++) {
    Serial.print(payload[i]);
  }
  Serial.println();

  for(int i = 0; i < 5; i++) {  // we first take 5 pictures, as the quality improves with more pictures
    camera_fb_t *fb = esp_camera_fb_get();
    delay(100);
    esp_camera_fb_return(fb);
  }
  
  // Take final photo and send it
  sendPhoto(); 
}

void loop() {
  client.loop();
}


void sendPhoto() {
  digitalWrite(4, HIGH);    // light

  // Take Picture with Camera
  camera_fb_t *fb = NULL;
  fb = esp_camera_fb_get();

  digitalWrite(4, LOW);   // light
  delay(5000);
  if (!fb){
    Serial.println("Camera capture failed");
    return;
  }

  HTTPClient http;
  Serial.print("[HTTP] Begin POST \n");
  http.begin(post_url);
  int httpCode = http.sendRequest("POST", fb->buf, fb->len); // we simply put the whole image in the post body.

  if (httpCode > 0){
    Serial.printf("[HTTP] POST code: %d\n", httpCode);

    if (httpCode == HTTP_CODE_OK){
      String payload = http.getString();
      Serial.println(payload);
    }
  }else{
    Serial.printf("[HTTP] POST failed, error: %s\n", http.errorToString(httpCode).c_str());
    ESP.restart();
  }

  http.end();
  esp_camera_fb_return(fb);
  startMQTT();  // restart MQTT after sending Image
}

void startMQTT(){
  if(client.connect("CAM")){
    Serial.println("CAM - MQTT - OK");
    client.subscribe("esp_cam_0");
  }else{
    Serial.println("CAM - MQTT - ERROR");
    delay(1000);
    ESP.restart();
  }
}