int Screen_precision = 0, Console_precision = 0, Controller1_precision = 0;

float myVariable;

event ServButt = event();

// "when started" hat block
int whenStarted1() {
  while (true) {
    Brain.Screen.setCursor(1, 1);
    Brain.Screen.print(printToScreen_numberFormat(), static_cast<float>(Brain.Battery.capacity()));
    Brain.Screen.setCursor(3, 1);
    Brain.Screen.print("VEXcode");
    Brain.Screen.clearLine(1);
    Brain.Screen.setCursor(Brain.Screen.row(), 1);
    Brain.Screen.clearLine(3);
    Brain.Screen.setCursor(Brain.Screen.row(), 1);
    wait(5.0, seconds);
  wait(5, msec);
  }
  return 0;
}

// "when Controller1 ButtonRight pressed" hat block
void onevent_Controller1ButtonRight_pressed_0() {
  ServoA.setPosition(70.0 - 50.0, degrees);
  printf("SER180N");
  Controller1.Screen.setCursor(1, 1);
  Controller1.Screen.print("SER180NL");
  ServButt.broadcast();
  printf("SER180P");
  Controller1.Screen.setCursor(1, 1);
  Controller1.Screen.print("SER180PR");
  ServButt.broadcast();
}

// "when Controller1 ButtonA pressed" hat block
void onevent_Controller1ButtonA_pressed_0() {
  ServoB.setPosition(90.0 - 50.0, degrees);
}

// "when Controller1 ButtonA released" hat block
void onevent_Controller1ButtonA_released_0() {
  ServoB.setPosition(-230.0 - 50.0, degrees);
}

// "when Controller1 ButtonR1 pressed" hat block
void onevent_Controller1ButtonR1_pressed_0() {
  MC55_4.spin(forward, 6.0, volt);
}

// "when Controller1 ButtonR1 released" hat block
void onevent_Controller1ButtonR1_released_0() {
  MC55_4.stop();
}

// "when Controller1 ButtonR2 pressed" hat block
void onevent_Controller1ButtonR2_pressed_0() {
  MC55_4.spin(reverse, 6.0, volt);
}

// "when Controller1 ButtonR2 released" hat block
void onevent_Controller1ButtonR2_released_0() {
  MC55_4.stop();
}

// "when Controller1 ButtonL1 pressed" hat block
void onevent_Controller1ButtonL1_pressed_0() {
  MC55_arm.spin(forward, 4.0, volt);
}

// "when Controller1 ButtonL1 pressed" hat block
void onevent_Controller1ButtonL1_pressed_1() {
  MC55_arm.spin(forward, 4.0, volt);
}

// "when Controller1 ButtonL1 released" hat block
void onevent_Controller1ButtonL1_released_0() {
  MC55_arm.setStopping(brake);
  MC55_arm.stop();
}

// "when Controller1 ButtonL1 released" hat block
void onevent_Controller1ButtonL1_released_1() {
  MC55_arm.setStopping(brake);
  MC55_arm.stop();
}

// "when started" hat block
int whenStarted2() {
  Controller1.Screen.clearScreen();
  while (true) {
    Controller1.Screen.setCursor(2, 1);
    Controller1.Screen.print("Batt.");
    Controller1.Screen.setCursor(4, 1);
    Controller1.Screen.print(printToController1_numberFormat(), static_cast<float>(Brain.Battery.capacity()));
    wait(0.5, seconds);
    Controller1.Screen.setCursor(2, 14);
    Controller1.Screen.print("Drv. W");
    Controller1.Screen.clearLine(4);
    Controller1.Screen.setCursor(Controller1.Screen.row(), 1);
    Controller1.Screen.setCursor(4, 16);
    Controller1.Screen.print(printToController1_numberFormat(), static_cast<float>(Drivetrain.power()));
    wait(0.5, seconds);
    Controller1.Screen.clearLine(4);
    Controller1.Screen.setCursor(Controller1.Screen.row(), 1);
    Controller1.Screen.setCursor(2, 16);
    Controller1.Screen.setCursor(4, 10);
    wait(0.5, seconds);
    Controller1.Screen.clearLine(4);
    Controller1.Screen.setCursor(Controller1.Screen.row(), 1);
  wait(5, msec);
  }
  return 0;
}

// "when Controller1 ButtonL2 pressed" hat block
void onevent_Controller1ButtonL2_pressed_0() {
  MC55_arm.spin(reverse, 1.5, volt);
}

// "when Controller1 ButtonL2 released" hat block
void onevent_Controller1ButtonL2_released_0() {
  MC55_arm.setStopping(brake);
  MC55_arm.stop();
}

// "when started" hat block
int whenStarted3() {
  while (true) {
    if (Brain.Battery.capacity() < 20.0) {
      repeat(30) {
        Controller1.Screen.setCursor(1, 10);
        Controller1.Screen.print("BATT LOW");
        Controller1.Screen.newLine();
        Controller1.rumble("....");
        wait(30.0, seconds);
        Controller1.Screen.clearLine(1);
        Controller1.Screen.setCursor(Controller1.Screen.row(), 1);
        wait(5, msec);
      }
    }
  wait(5, msec);
  }
  return 0;
}

// "when I receive ServButt" hat block
void onevent_ServButt_0() {
}

// "when I receive ServButt" hat block
void onevent_ServButt_1() {
  wait(2.0, seconds);
  Controller1.Screen.clearScreen();
  Controller1.Screen.setCursor(1, 1);
}

// "when Controller1 ButtonLeft pressed" hat block
void onevent_Controller1ButtonLeft_pressed_0() {
  ServoA.setPosition(-180.0 - 50.0, degrees);
  printf("SER180N");
  Controller1.Screen.setCursor(1, 1);
  Controller1.Screen.print("SER180NR");
  ServButt.broadcast();
}


int main() {
  // Initializing Robot Configuration. DO NOT REMOVE!
  vexcodeInit();

  // register event handlers
  Controller1.ButtonRight.pressed(onevent_Controller1ButtonRight_pressed_0);
  Controller1.ButtonA.pressed(onevent_Controller1ButtonA_pressed_0);
  Controller1.ButtonA.released(onevent_Controller1ButtonA_released_0);
  Controller1.ButtonR1.pressed(onevent_Controller1ButtonR1_pressed_0);
  Controller1.ButtonR1.released(onevent_Controller1ButtonR1_released_0);
  Controller1.ButtonR2.pressed(onevent_Controller1ButtonR2_pressed_0);
  Controller1.ButtonR2.released(onevent_Controller1ButtonR2_released_0);
  Controller1.ButtonL1.pressed(onevent_Controller1ButtonL1_pressed_0);
  Controller1.ButtonL1.pressed(onevent_Controller1ButtonL1_pressed_1);
  Controller1.ButtonL1.released(onevent_Controller1ButtonL1_released_0);
  Controller1.ButtonL1.released(onevent_Controller1ButtonL1_released_1);
  Controller1.ButtonL2.pressed(onevent_Controller1ButtonL2_pressed_0);
  Controller1.ButtonL2.released(onevent_Controller1ButtonL2_released_0);
  ServButt(onevent_ServButt_0);
  ServButt(onevent_ServButt_1);
  Controller1.ButtonLeft.pressed(onevent_Controller1ButtonLeft_pressed_0);

  wait(15, msec);
  vex::task ws1(whenStarted2);
  vex::task ws2(whenStarted3);
  whenStarted1();
}
