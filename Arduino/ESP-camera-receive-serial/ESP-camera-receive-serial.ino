// this sample code provided by www.programmingboss.com
#define RXp2 16
#define TXp2 17

int count = 0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin(1000000);
  Serial2.begin(1000000, SERIAL_8N1, RXp2, TXp2);
}
void loop() {
  char b = Serial2.read();
  Serial.print(b);
  if(b == 'R') {
    count++;
    b = Serial2.read();
    if(b == 'D') {
      count++;
      b = Serial2.read();
      if(b == 'Y') {
        count++;
        Serial.println();
        Serial.print("image");
        Serial.println(count);
        Serial.println();
        count = 0;
      }
    }
  } else {
    count++;
  }
  //for(int i = 0; i < 8; i++) {
    //Serial.print(bitRead(b, i));
  //}
}