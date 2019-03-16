// Ultrasonic Sensor & IR
// versio 0.0.2

//sonic1
int triggerPin = 11;      //Define IO pins
int echoPin = 13;

//sonic2
int triggerPin2 = 10;      //Define IO pins
int echoPin2 = 12;

//sonic3
int triggerPin3 = 9;      //Define IO pins
int echoPin3 = 8;

// IR sensors
int ir1 = 2;
int ir2 = 3;
int ir3 = 4;
int ir4 = 5;


long duration;
double distance;

long duration2;
double distance2;

long duration3;
double distance3;

//float v=331.5+0.6*20; // 20-temperature of air

void setup()
{
  pinMode(triggerPin, OUTPUT);   //Define pin
  pinMode(echoPin, INPUT);
  pinMode(triggerPin2, OUTPUT);   //Define pin
  pinMode(echoPin2, INPUT);  
  Serial.begin(9600);           //Starts the serial communication
}

void loop()
{
  digitalWrite(triggerPin, LOW);   //Reset the trigger pin
  delay(1000);
  digitalWrite(triggerPin, HIGH);     //Create a 10 micro second pulse
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  duration = pulseIn(echoPin, HIGH); //Read the pulse travel time in microseconds.
  distance= duration*0.0344/2;        //Calculate the distance - speed of sound is 0.034 cm per microsecond
  //Serial.print("Distance 1: ");        //Display the distance on the serial monitor
  //Serial.println(distance);
  pulseIn(echoPin, LOW);

  digitalWrite(triggerPin2, LOW);   //Reset the trigger pin
  //delay(200);
  digitalWrite(triggerPin2, HIGH);     //Create a 10 micro second pulse
  delayMicroseconds(10);
  digitalWrite(triggerPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH); //Read the pulse travel time in microseconds.
  distance2= duration2*0.0344/2;        //Calculate the distance - speed of sound is 0.034 cm per microsecond

  digitalWrite(triggerPin3, LOW);   //Reset the trigger pin
  //delay(200);
  digitalWrite(triggerPin3, HIGH);     //Create a 10 micro second pulse
  delayMicroseconds(10);
  digitalWrite(triggerPin3, LOW);
  duration3 = pulseIn(echoPin3, HIGH); //Read the pulse travel time in microseconds.
  distance3= duration3*0.0344/2;        //Calculate the distance - speed of sound is 0.034 cm per microsecond

  Serial.print("Distance 1: ");        //Display the distance on the serial monitor
  Serial.print(distance);
  Serial.print(" ; ");
  Serial.print("Distance 2: ");        //Display the distance on the serial monitor
  Serial.print(distance2);
  Serial.print(" ; ");
  Serial.print("Distance 3: ");        //Display the distance on the serial monitor
  Serial.print(distance3);
  Serial.print(" ; ");
  Serial.print("IR1 : ");
  Serial.print(digitalRead(ir1));
  Serial.print(" ; ");
  Serial.print("IR2 : ");
  Serial.print(digitalRead(ir2));
  Serial.print(" ; ");
  Serial.print("IR3 : ");
  Serial.print(digitalRead(ir3));
  Serial.print(" ; ");
  Serial.print("IR4 : ");
  Serial.println(digitalRead(ir4));  
}
