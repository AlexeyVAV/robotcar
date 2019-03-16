#include <Servo.h>

Servo myservo;  // create servo object to control a servo

 // servo setup
int pos = 171;    // variable to store the servo position
int pos_var = 1;
const int servo_pin = 9; // Arduino pin to control servo
const int buttonPin = 2; // Button pin

// set up buttonState
int buttonState = 0;

// Canon shoot command from Serial
int shoot_comand = 0;

// sonic setup
const int sonicTriggerPin = 10;      //Define IO pins
const int sonicEchoPin = 12;

void setup() {
  Serial.begin(9600);
  myservo.attach(servo_pin);  // attaches the servo on pin 9 to the servo object
  myservo.write(pos);

  // initialize ultrasonic pins
  pinMode(sonicTriggerPin, OUTPUT);
  pinMode(sonicEchoPin, INPUT);

  // initialize the pushbutton pin as an input:
  pinMode(buttonPin, INPUT);
}


void shoot() {

  myservo.write(pos_var - 170);
  delay(1000);
  myservo.write(pos_var + 170);

}

void loop() {

  // Serial command shoot
   while(Serial.available()) {

      shoot_comand= Serial.parseInt();// read the incoming data as string

      Serial.println(shoot_comand);

      if (shoot_comand == 1) {
        Serial.println("Shoot");
        shoot();
      }
   }

   // manual shoot
   buttonState = digitalRead(buttonPin);

   if (buttonState == HIGH) {
       shoot();
   }

   // Ultrasonic
   // calculate time to obstacle 
   digitalWrite(sonicTriggerPin, LOW);   //Reset the trigger pin
   delay(1000);
   digitalWrite(sonicTriggerPin, HIGH);     //Create a 10 micro second pulse
   delayMicroseconds(10);
   digitalWrite(sonicTriggerPin, LOW);
   duration1 = pulseIn(sonicEchoPin, HIGH); //Read the pulse travel time in microseconds.
   distance1 = duration1*0.0344/2;        //Calculate the distance - speed of sound is 0.034 cm per microsecond
   pulseIn(sonicEchoPin, LOW);

}
