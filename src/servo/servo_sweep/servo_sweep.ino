
#include <Servo.h>

Servo myservo;  // create servo object to control a servo

int pos = 171;    // variable to store the servo position
int pos_var = 1;

const int servo_pin = 9; // Arduino pin to control servo
const int buttonPin = 2; // Button pin

int buttonState = 0; 

int a = 0;

void setup() {
  Serial.begin(9600);
  myservo.attach(servo_pin);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos);

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}

void shoot() {

  myservo.write(pos_var - 170);
  delay(1000);
  myservo.write(pos_var + 170);

}

void loop() {
   while(Serial.available()) {
    
      a= Serial.parseInt();// read the incoming data as string
    
      Serial.println(a);

      if (a == 1) {
        Serial.println("Shoot");
        shoot();
      }
   }

   buttonState = digitalRead(buttonPin);

   if (buttonState == HIGH) {
       shoot();
   }

}
