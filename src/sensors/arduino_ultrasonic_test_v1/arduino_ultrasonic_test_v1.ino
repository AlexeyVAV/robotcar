// Ultrasonic Sensor
//https://www.the-diy-life.com/connecting-an-ultrasonic-sensor-to-an-arduino/
// versio 0.0.0

int triggerPin = 11;      //Define IO pins
int echoPin = 13;

int triggerPin2 = 10;      //Define IO pins
int echoPin2 = 12;

long duration;
double distance;

long duration2;
double distance2;

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
  delay(200);
  digitalWrite(triggerPin, HIGH);     //Create a 10 micro second pulse
  delayMicroseconds(10);
  digitalWrite(triggerPin, LOW);
  duration = pulseIn(echoPin, HIGH); //Read the pulse travel time in microseconds.
  distance= duration*0.0344/2;        //Calculate the distance - speed of sound is 0.034 cm per microsecond
  Serial.print("Distance 1: ");        //Display the distance on the serial monitor
  Serial.println(distance);
  pulseIn(echoPin, LOW);

  digitalWrite(triggerPin2, LOW);   //Reset the trigger pin
  delay(200);
  digitalWrite(triggerPin2, HIGH);     //Create a 10 micro second pulse
  delayMicroseconds(10);
  digitalWrite(triggerPin2, LOW);
  duration2 = pulseIn(echoPin2, HIGH); //Read the pulse travel time in microseconds.
  distance2= duration2*0.0344/2;        //Calculate the distance - speed of sound is 0.034 cm per microsecond
  Serial.print("Distance 2: ");        //Display the distance on the serial monitor
  Serial.println(distance2);
    
}
