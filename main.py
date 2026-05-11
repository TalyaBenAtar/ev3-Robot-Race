#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Objects:

ev3 = EV3Brick()

gyro_sensor = GyroSensor(Port.S1)
csensor = ColorSensor(Port.S2)

motor_right = Motor(Port.A) # positiive - clockwise, negative- counter clockwise
motor_left = Motor(Port.B)



# Parameters:

SPEED = 1200
TURN_SPEED = 700
DARK_THRESHOLD = 4

TURN_ANGLE = 180
WHEEL_DIAMETER = 53   # TODO measure the wheel diameter in mm
AXLE_TRACK = 191      # TODO measure distance between wheel centers in mm

# TODO If the robot "snakes" or wobbles violently, lower that factor to 1 or 2. 
# If the robot drifts too much to one side, increase that factor to 10 or 20.
CORRECTION_FACTOR = 0.5
    
# TODO If the robot gets stuck on the line, increase the max_distance to 300 or 400. 
# If the robot goes too far after leaving the line, decrease that value to 100 or 150.
LEAVE_LINE_MAX_DISTANCE = 400 # maximum distance in degrees of wheel rotation
MAX_CORRECTION = 200



#functions:

# TODO Test the color sensor readings
def test_color_sensor():
    while True:
        print(csensor.reflection())
        wait(200)


#stop both motors
def stop_motors():
    motor_left.stop()
    motor_right.stop()


# Drive forward until dark finish line with gyro correction
def drive_until_dark_line():
    gyro_sensor.reset_angle(0)

    while True:
        angle = gyro_sensor.angle()
        correction = angle * CORRECTION_FACTOR
        correction = max(min(correction, MAX_CORRECTION), -MAX_CORRECTION)  # limit the correction to the maximum value

        motor_left.run(-SPEED + correction)
        motor_right.run(-SPEED - correction)

        # darkness goes from 0 (black) to 100 (white), so we check if it's below the threshold to detect the dark line
        if csensor.reflection() < DARK_THRESHOLD:
            stop_motors()
            break

        wait(10)


# Turn around 180 degrees using wheel/axle calculation
def turn_around_180():
    motor_degrees = TURN_ANGLE * AXLE_TRACK / WHEEL_DIAMETER

    motor_left.run_angle(-TURN_SPEED, motor_degrees, wait=False)
    motor_right.run_angle(-TURN_SPEED, -motor_degrees, wait=True)

    stop_motors()
    wait(200)


# Turn around 180 degrees using gyro sensor
def gyro_turn():
    gyro_sensor.reset_angle(0)

    while abs(gyro_sensor.angle()) < TURN_ANGLE - 5:
        motor_left.run(TURN_SPEED)
        motor_right.run(-TURN_SPEED)
        wait(10)
    
    stop_motors()
    wait(200)


# Move away from the finish line before searching for the start line
def leave_dark_line():
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)

    # Move forward until we are off the dark line, allowing a maximum distance of 200 degrees of wheel rotation to prevent getting stuck or going too far
    while (csensor.reflection() < DARK_THRESHOLD or (abs(motor_left.angle()) + abs(motor_right.angle())) / 2 < LEAVE_LINE_MAX_DISTANCE):
        motor_left.run(-SPEED)
        motor_right.run(-SPEED)
        wait(10)

    stop_motors()
    wait(100)


# main flow of the program:
def main():
    ev3.speaker.beep()

    # Uncomment this only when testing sensor values:
    # test_color_sensor()

    drive_until_dark_line()

    wait(100)
    turn_around_180()
    # gyro_turn()

    leave_dark_line()
    drive_until_dark_line()

    ev3.speaker.beep()


main()



