// Ultrasonic Sensor
//https://www.the-diy-life.com/connecting-an-ultrasonic-sensor-to-an-arduino/
// versio 0.0.0

int triggerPin = 11;      //Define IO pins
int echoPin = 13;

long duration;
double distance;

void setup()
{
  pinMode(triggerPin, OUTPUT);   //Define pin
  pinMode(echoPin, INPUT);
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
  Serial.print("Distance: ");        //Display the distance on the serial monitor
  Serial.println(distance);
}
