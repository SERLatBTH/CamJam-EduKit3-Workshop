# Help Mechanical Engineers Prototype a Robot

Welcome to the workshop! Today, you'll take on the role of a software engineer consulting for a team of mechanical engineers who need help prototyping their robot. Your mission is to identify and solve problems in their robot’s functionality by programming its sensors and actuators.

The robot consists of:
- **A Raspberry Pi** as the processor
- **Two motors attached to wheels** as actuators
- **A distance sensor** to detect objects

We will use the Raspberry Pi to connect to the robot via SSH, allowing us to program and test its features remotely. By the end of this workshop, you’ll write a report about what works, what needs improvement, and how the robot can be optimized. [Write your report here](report.md).

This workshop focuses on understanding software as a tool for communication and problem-solving, not just coding. Don’t worry if you’re new to programming—we’ll explain everything step by step, including concepts like variables, loops, and if-statements. Let’s get started!



## Workshop Overview

Here are the steps we’ll follow:
1. **Understand the Robot**: Learn about its components and functionality.
2. **Write and Test Code**: Identify issues and program solutions. Clickable links will take you directly to the files you’ll edit.
3. **Write a Report**: Document your findings and propose improvements. [Start your report here](report.md).



## Understanding the Robot

### The Raspberry Pi
The Raspberry Pi is a small, affordable computer that serves as the "brain" of the robot. It allows us to write and execute Python code, controlling the motors and reading data from the distance sensor.

### Python Programming
Python is a beginner-friendly programming language. Think of it as giving clear, step-by-step instructions to the robot in a language it understands.

### SSH
SSH (Secure Shell) lets us connect to the Raspberry Pi from another computer over a network. Using a terminal command like `runonrobot [filename]`, we can run Python files directly on the robot.



## Getting Started with Python
We’ll start by writing a simple Python program to print a message.

### Hello World
1. Open the file named **`helloworld.py`**.
2. Type the following code:
   ```python
   print("Hello, World!")
   ```
3. Save the file and run it on the robot by typing:
   ```
   runonrobot helloworld.py
   ```
   You should see the message "Hello, World!" printed in the terminal. Remember, it’s the robot that runs the code, so the message is being generated on the robot and sent back to your computer through the SSH connection.

[Edit helloworld.py](helloworld.py)



## Key Concepts in Python

### Variables
Variables store information. Think of them like containers that hold data:
```python
name = "Your Name"
print(name)
```
Here, the variable `name` holds the text "Your Name." Try editing **`helloworld.py`** to include a variable and print its value. [Edit helloworld.py](helloworld.py)

### Loops
Loops allow repetition. For example, let’s make the robot count numbers:
```python
count = 0
while True:
    count += 1
    print(count)
```
This code will count endlessly. To stop the program, press CTRL+C in the terminal to interrupt it.

### Libraries and Timing
To slow the counting loop, we’ll use the `time` library:
```python
import time
count = 0
while True:
    count += 1
    print(count)
    time.sleep(1)  # Wait for 1 second
```
[Edit helloworld.py](helloworld.py)

### Functions and If-Statements
Functions group reusable code. Here’s a function to check if a number is even:
```python
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

print(is_even(4))  # This will print True
```
Modify your counting loop to only print even numbers:
```python
while True:
    count += 1
    if is_even(count):
        print(count)
    time.sleep(1)
```
[Edit helloworld.py](helloworld.py)



## Programming the Robot

### Task 1: Controlling the Motors
Open the next file called **`motors.py`**:
```python
import time
from gpiozero import CamJamKitRobot

robot = CamJamKitRobot()
robot.forward()
time.sleep(1)
robot.stop()
```
This code makes the robot move forward for one second and then stop. Run the file:
```bash
runonrobot motors.py
```
[Edit motors.py](motors.py)

### Task 2: Driving and Turning
Extend **`motors.py`** to include turning:
```python
robot.backward()
time.sleep(1)
robot.left()
time.sleep(0.5)
robot.right()
time.sleep(0.5)
```
[Edit motors.py](motors.py)

### Task 3: Speed Calibration
Add a `speed` variable to control the robot’s speed:
```python
speed = 0.5
robot.forward(speed)
time.sleep(1)
robot.stop()
```
[Edit motors.py](motors.py)

### Task 4: Using the Distance Sensor
Open the file named **`distance.py`**:
```python
import time
from gpiozero import DistanceSensor

sensor = DistanceSensor(echo=18, trigger=17)
while True:
    distance = sensor.distance * 100
    print("Distance:", distance, "cm")
    time.sleep(1)
```
This code measures and prints the distance detected by the sensor. Can you detect any issues with it? Run it:
```bash
runonrobot distance.py
```
[Edit distance.py](distance.py)

### Task 5: Obstacle Avoidance Robot
The mechanical engineers have attempted to create an obstacle avoidance program for the robot, but it has some issues that need to be fixed. Your task is to review and correct their code. Open the file **`obstacle_avoidance.py`** and examine the following code:
```python
import time
from gpiozero import CamJamKitRobot, DistanceSensor

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=18, trigger=17)
speed = 1.0
detect_distance = 10

while True:
    robot.forward(speed)
    print(sensor.distance * 100 + " cm")
    time.sleep(1)
    if sensor.distance * 100 < detect_distance:
        robot.stop()
        robot.backward(speed)
        time.sleep(1)
        robot.left(speed)
        time.sleep(speed)
```
[Edit obstacle_avoidance.py](obstacle_avoidance.py)



## Final Task: Write a Report
After testing your robot, document your findings:
- **Issues Identified:** List problems with the robot.
- **Solutions Implemented:** Explain the code you wrote and its purpose.
- **Recommendations:** Provide suggestions for improvements for both code and robot.

Write your report in the provided file: [Write your report here](report.md).
