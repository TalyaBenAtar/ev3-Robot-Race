# 🤖 EV3 Line Return Robot  
_A LEGO MINDSTORMS EV3 robot that drives to a dark line, turns around, and returns back_

---

## 📖 Description

This project controls a **LEGO MINDSTORMS EV3** robot using **Pybricks MicroPython**.

The robot drives forward while using a **gyro sensor** to keep itself straight.  
When it detects a dark line using the **color sensor**, it stops, turns around, moves away from the line, and searches for the line again from the other direction.

In simple words:  
the robot drives to a finish line, turns around, and comes back. Tiny robot taxi behavior. Very official.

---

## 🌟 Features

- Drives forward until detecting a dark line.
- Uses gyro correction to reduce drifting.
- Supports two turn methods:
  - 180° turn using wheel and axle measurements.
  - 180° turn using the gyro sensor.
- Uses a color sensor to detect the dark line.
- Includes a test function for checking color sensor reflection values.
- Includes adjustable parameters for different robot builds.

---

## 🧱 Robot Platform

This code is designed for a:

**LEGO MINDSTORMS EV3 programmable robot**

Recommended environment:

- LEGO EV3 Brick
- LEGO EV3 motors
- LEGO EV3 sensors
- Pybricks MicroPython v2.0 or higher

---

## 🔌 Motors and Sensors Used

### 🧠 EV3 Brick
```python
ev3 = EV3Brick()
```

### 🌀 Gyro Sensor
Connected to:

```python
Port.S1
```

Used for:
- Keeping the robot driving straight.
- Optional 180° gyro-based turning.

### 🎨 Color Sensor
Connected to:

```python
Port.S2
```

Used for:
- Detecting the dark line using reflected light values.

### ⚙️ Right Motor
Connected to:

```python
Port.A
```

### ⚙️ Left Motor
Connected to:

```python
Port.B
```

---

## 🧰 Tech Stack

- **Language:** Pybricks MicroPython
- **Robot:** LEGO MINDSTORMS EV3
- **IDE / Editor:** Visual Studio Code with the EV3 MicroPython extension
- **Runtime:** LEGO EV3 MicroPython v2.0 or higher

---

## 📸 Robot Media

Add pictures and videos of the robot here after uploading them to GitHub.

### Robot Pictures

```html
<img src="YOUR_ROBOT_IMAGE_LINK_HERE" width="350"/>
```

### Demo Video

```md
[Watch the robot demo](YOUR_VIDEO_LINK_HERE)
```

---

## ⚙️ How the Program Works

### 1. Start
The EV3 brick makes a beep to show the program started.

```python
ev3.speaker.beep()
```

### 2. Drive Until Dark Line
The robot drives forward while reading the gyro angle.

If the robot drifts, the gyro correction adjusts the motor speeds.

```python
drive_until_dark_line()
```

The robot stops when:

```python
csensor.reflection() < DARK_THRESHOLD
```

### 3. Turn Around
The robot turns 180°.

Default method:

```python
turn_around_180()
```

Alternative gyro-based method:

```python
gyro_turn()
```

### 4. Leave the Line
The robot moves forward until it is no longer on the dark line.

```python
leave_dark_line()
```

### 5. Return
The robot drives again until it finds the dark line from the other direction.

```python
drive_until_dark_line()
```

### 6. Finish
The EV3 brick beeps again.

---

## 🚀 Getting Started

### 1. Install the EV3 MicroPython Extension

Use **Visual Studio Code** and install the official EV3 MicroPython / Pybricks extension.

### 2. Prepare the EV3 Brick

Make sure your EV3 brick is running:

```text
LEGO EV3 MicroPython v2.0 or higher
```

### 3. Connect the Hardware

Connect the motors and sensors exactly like this:

| Component | Port |
|---|---|
| Gyro Sensor | S1 |
| Color Sensor | S2 |
| Right Motor | A |
| Left Motor | B |

### 4. Upload the Code

Upload the Python file to the EV3 brick.

### 5. Place the Robot

Place the robot on a surface with:
- A clear light-colored path.
- A dark line that the color sensor can detect.

### 6. Run the Program

Run the file from VS Code or directly from the EV3 brick.

---

## 🎛️ Parameters to Adjust

Different EV3 robot builds behave differently, so these values may need calibration.

### Speed

```python
SPEED = 1200
```

Controls forward driving speed.

Lower it if:
- The robot is too fast.
- The robot misses the dark line.
- The robot becomes unstable.

---

### Turn Speed

```python
TURN_SPEED = 700
```

Controls how fast the robot turns.

Lower it if:
- The robot overshoots the turn.
- The robot turns too aggressively.

---

### Dark Line Threshold

```python
DARK_THRESHOLD = 4
```

Controls when the robot detects the dark line.

Use this function to test values:

```python
test_color_sensor()
```

If the dark line gives a reflection value of 8, for example, set the threshold slightly above it:

```python
DARK_THRESHOLD = 10
```

---

### Turn Angle

```python
TURN_ANGLE = 180
```

The target turning angle.

Usually this should stay at 180.

---

### Wheel Diameter

```python
WHEEL_DIAMETER = 53
```

The wheel diameter in millimeters.

Measure your own wheels and update this value if needed.

---

### Axle Track

```python
AXLE_TRACK = 191
```

The distance between the centers of the two wheels, in millimeters.

This value is important for accurate turning.

---

### Correction Factor

```python
CORRECTION_FACTOR = 0.5
```

Controls how strongly the robot corrects itself using the gyro.

If the robot wobbles too much, lower it.

If the robot drifts too much, increase it.

---

### Leave Line Distance

```python
LEAVE_LINE_MAX_DISTANCE = 400
```

Controls how far the robot can move after detecting the dark line.

Increase it if:
- The robot gets stuck on the line.

Decrease it if:
- The robot moves too far after leaving the line.

---

### Maximum Correction

```python
MAX_CORRECTION = 200
```

Limits the correction applied to the motors.

This prevents the robot from overcorrecting too aggressively.

---

## 🧪 Sensor Calibration

Before running the full program, test the color sensor:

```python
test_color_sensor()
```

Check the printed reflection values for:

| Surface | Expected Value |
|---|---|
| White / light surface | Higher value |
| Black / dark line | Lower value |

Then adjust:

```python
DARK_THRESHOLD
```

The threshold should be higher than the dark line value and lower than the light surface value.

---

## 🧭 Turn Options

The code includes two turning options.

### Option 1: Wheel-Based Turn

```python
turn_around_180()
```

Uses:

```python
WHEEL_DIAMETER
AXLE_TRACK
TURN_ANGLE
```

This requires accurate robot measurements.

### Option 2: Gyro-Based Turn

```python
gyro_turn()
```

Uses the gyro sensor to stop when the robot reaches about 180°.

To use it, replace:

```python
turn_around_180()
```

with:

```python
gyro_turn()
```

---

## 📁 Main Code Flow

```python
def main():
    ev3.speaker.beep()

    drive_until_dark_line()

    wait(100)
    turn_around_180()
    # gyro_turn()

    leave_dark_line()
    drive_until_dark_line()

    ev3.speaker.beep()
```

---

## ⚠️ Notes

- The robot must have two drive motors.
- The color sensor must face the floor.
- The gyro sensor should be still when the program starts.
- The robot should start on a light surface, not directly on the dark line.
- Motor directions may need to be changed depending on how the motors are mounted.

If the robot drives backward or turns the wrong way, change the motor speed signs in the movement functions.

---

## 🛠️ Future Improvements

- Add better line-leaving logic.
- Add a button-controlled start.
- Add screen messages on the EV3 brick.
- Add automatic calibration for the color sensor.
- Add support for different line colors.
- Add a more accurate PID controller for smoother driving.

---

## 🤖 Final Result

This project demonstrates a simple but useful autonomous EV3 behavior:

> Drive straight, detect a target line, turn around, and return.

Small robot. Big confidence.
