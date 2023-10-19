int inputPin = 8;    // choose the input pin (for PIR sensor)
int pirState = LOW;  // we start, assuming no motion detected
int val = 0;         // variable for reading the pin status

void setup() {
  pinMode(inputPin, INPUT);

  Serial.begin(9600);
}

void loop() {
  val = digitalRead(inputPin);

  if (val == HIGH)
  {
    if (pirState == LOW) {
      Serial.println("Motion detected!");
      pirState = HIGH;
    }
  } else {
    if (pirState == HIGH) {
      Serial.println("Motion ended!");
      pirState = LOW;
    }
  }
}