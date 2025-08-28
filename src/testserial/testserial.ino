#include <EVN.h>

EVNAlpha board;
EVNMotor backmotor(3, EV3_MED);
EVNMotor frontmotor(1, EV3_MED);
EVNDistanceSensor righttof(5, 33);
EVNDistanceSensor lefttof(8, 33);
float Kp = 0.5;

void setup() {
    board.begin();
    Serial.begin(115200);
    Serial2.begin(9600);
    delay(1000);
    righttof.begin();
    lefttof.begin();
}

void setup1() {
    backmotor.begin();
    frontmotor.begin();
}

void loop() {
    // uint16_t rightdist = righttof.read(true);
    // uint16_t leftdist = lefttof.read(true);
    // Serial.println("righttof: ");
    // Serial.println(rightdist);
    // Serial.println(" mm");

    // Serial.println("lefttof: ");
    // Serial.println(leftdist);
    // Serial.println(" mm");
     if (Serial2.available()) {
        int incomingChar = Serial2.read();
        Serial.println(incomingChar, DEC);
        // Serial.println("something");
      }
      else {
        Serial.println("nothing");
      }
      delay(1000);

      //for test code, it should just print 0 
}

//positive angle, turn right
//negative anle, turn left 
// void jajaj() {
//     uint16_t rightdist = righttof.read(true);
//     uint16_t leftdist = lefttof.read(true);
//     int error = rightdist - leftdist; // if neg, then closer to rightwall
//     int steer = Kp*error;
//     // if (steer > 20) {
//     //     steer = 20;
//     // }
//     // if (steer < -20) {
//     //     steer = -20;
//     // }
//     Serial.println(steer);
//     // frontmotor.runPosition(300,steer, false);
// }