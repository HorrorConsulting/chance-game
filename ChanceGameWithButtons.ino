/*
  Chance Game Button controller 

  This is example code for controlling five LEDs 
  and sequences their actions.

  Based on “Fading” example 
  created 1 Nov 2008
  by David A. Mellis
  And modified 30 Aug 2011
  by Tom Igoe

  LED button controller code by HorrorConsulting.com
 
*/

int Blue = 12;    // LED connected to digital pin 8
int Green = 11;    // LED connected to digital pin 10
int Yellow = 10;    // LED connected to digital pin 9
int White = 8;    // LED connected to digital pin 11
int Red = 9;    // LED connected to digital pin 12

long RandNum;   // I think this line can be removed

void setup() {
  randomSeed(analogRead(0));
}

void loop() {
BlinkRandom(20);
BlinkAround(4);
BlinkUpDown(4);
BlinkRandom(20);
FancyRampUpDown();
BlinkRandom(20);
BlinkSeq(5);
BlinkSeqRev(5);
BlinkRandom(20);
RampUpDown();

}

void Blink(int pin){
     analogWrite(pin, 100);
    // wait for 200 milliseconds 
    delay(200);
    analogWrite(pin, 0);
    // wait for 200 milliseconds 
    delay(200);
}

void RampUpDown(){
int timespan (1000);
int fadeValue = 150;
      analogWrite(White, fadeValue);
      delay(timespan);
      analogWrite(Red, fadeValue);
      delay(timespan);
      analogWrite(Yellow, fadeValue);
      delay(timespan);
      analogWrite(Green, fadeValue);
      delay(timespan);
      analogWrite(Blue, fadeValue);
    // wait for 1 second
    delay(1000);
fadeValue = 0;
      analogWrite(Blue, fadeValue);
      delay(timespan);
      analogWrite(Green, fadeValue);
      delay(timespan);
      analogWrite(Yellow, fadeValue);
      delay(timespan);
      analogWrite(Red, fadeValue);
      delay(timespan);
      analogWrite(White, fadeValue);
    // wait for 1 second
      delay(timespan); 
}


void FancyRampUpDown(){
  int timespan (1000);
  for (timespan = 1000 ; timespan >= 0 ; timespan -=200){
int fadeValue = 250;
      analogWrite(White, fadeValue);
      delay(timespan);
      analogWrite(Red, fadeValue);
      delay(timespan);
      analogWrite(Yellow, fadeValue);
      delay(timespan);
      analogWrite(Green, fadeValue);
      delay(timespan);
      analogWrite(Blue, fadeValue);
    // wait for the delay time
    delay(timespan);
fadeValue = 0;
      analogWrite(Blue, fadeValue);
      delay(timespan);
      analogWrite(Green, fadeValue);
      delay(timespan);
      analogWrite(Yellow, fadeValue);
      delay(timespan);
      analogWrite(Red, fadeValue);
      delay(timespan);
      analogWrite(White, fadeValue);
    // wait for the delay time
      delay(timespan); 
  }
}

void FadeUp(){
    // fade out from max to min in increments of 5 points:
  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    // sets the value (range from 0 to 255):
      analogWrite(White, fadeValue);
      delay(1000);
      analogWrite(Red, fadeValue);
      delay(1000);
      analogWrite(Yellow, fadeValue);
      delay(1000);
      analogWrite(Green, fadeValue);
      delay(1000);
      analogWrite(Blue, fadeValue);
  }

}

void FadeDown(){
    // fade out from max to min in increments of 5 points:
  for (int fadeValue = 255 ; fadeValue >= 0; fadeValue -= 5) {
    // sets the value (range from 0 to 255):
      analogWrite(White, fadeValue);
      delay(1000);
      analogWrite(Red, fadeValue);
      delay(1000);
      analogWrite(Yellow, fadeValue);
      delay(1000);
      analogWrite(Green, fadeValue);
      delay(1000);
      analogWrite(Blue, fadeValue);
  }
}

void BlinkSeqRev(int Blinks){
  for (int i = 0; i <= Blinks; i++){
    Blink(Blue);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(Green);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(Yellow);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(Red);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(White);
  }      
}

void BlinkSeq(int Blinks){
  for (int i = 0; i <= Blinks; i++){
    Blink(White);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(Red);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(Yellow);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(Green);
  }
  for (int i = 0; i <= Blinks; i++){
    Blink(Blue);
  }      
}

void BlinkAround(int Rounds){
  for (int i = 0; i <= Rounds; i++){
    Blink(White);
    Blink(Red);
    Blink(Yellow);
    Blink(Green);
    Blink(Blue);
  }      
}

void BlinkUpDown(int Rounds){
  for (int i = 0; i <= Rounds; i++){
    Blink(White);
    Blink(Red);
    Blink(Yellow);
    Blink(Green);
    Blink(Blue);
    Blink(Blue);
    Blink(Green);
    Blink(Yellow);
    Blink(Red);
    Blink(White);    
  }      
}

void BlinkRandom(int Rounds){
long RandNumber;
  for (int i = 0; i <= Rounds; i++){
    RandNumber = random(8,13);
    Blink(RandNumber);
  }
}

