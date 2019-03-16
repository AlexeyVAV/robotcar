// pinout defs
#define LS 2


void setup() {
  // put your setup code here, to run once:
  pinMode(LS, INPUT);
  Serial.begin(9600); 
}

void loop() {
  // put your main code here, to run repeatedly:
  Serial.print("Line signal : ");
  Serial.println(digitalRead(LS));
  delay(1000);
}
