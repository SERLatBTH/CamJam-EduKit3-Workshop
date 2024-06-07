
## **Overview and Introduction to Raspberry Pi**
Welcome to the coding part of this workshop! In this session, you'll learn how to program a robot using Python on a Raspberry Pi 4B. Don't worry if you're new to programming – we'll start from the basics and guide you through each step. By the end of the workshop, you'll be able to control your own robot using code!

## What is the raspberry pi?
The Raspberry Pi is a small, affordable computer that you can use to learn programming and create projects like robots, games, and more. It has input/output pins (GPIO pins) that allow you to connect and control external devices like motors and sensors. Think of it as the brain of your robot – you'll write code on the Raspberry Pi to tell your robot what to do. In this workshop we will use python to code on the pi.  Go to one of the desks with an already connected raspberry pi. 
## **Python:**
Python is a popular programming language known for its simplicity and readability. In this workshop, we'll use Python to write code for our robot. Don't worry if you've never coded before – Python is beginner-friendly! Think of it as giving instructions to your robot in a language it understands.
### SSH
In this workshop, we will make use of something called SSH (Secure Shell), which will allow us to connect to other computers (our robot in this case) over a network. We will use this to run our code on the robot by using a specially made command  called `runonrobot [write file name here]`. You will write this in a terminal to run the code. 
### **Getting Started**
In Python, we write code in a text editor or an integrated development environment (IDE). Don't worry if those terms sound confusing – they're just fancy ways of saying a place where we write  code. If you don't understand something or need help, just ask one of the instructors for help. 
- On your screen, you should see a visual studio code window open. This is where we will write our code
- We will write our code In the middle area.  To start off, we will use the command **"print()"** which will allow us to print text on the screen.
- Note that for every new command that you write, it is expected that you write it below previously written code.
#### Hello world
- Type the following command in the file: 
	**`print("Hello World!")`**
- Try running the code now by typing `runonrobot helloworld.py`  in a terminal window. It should show you the message "Hello world!" in the bottom section.  
<br>
<br>
<br> 
<br>
#### Variables
We can use **variables** in python to store information. Think of it like a container which can store different types of data like numbers and words. We will now write a new line under the print command.
- Let's create a variable called **'name'** and assign it a value:
	`name = "Write your name(s) here"` Write your names inside the quotation marks.
 - Now try printing the variable using print()! 
	`print(name)` You should see your names on the screen now. 
#### Counting 
A powerful feature in programming is repetition, which makes computers great at counting. We will write a new section under your print commands called a "while loop". 
- Create a new line under your print commands and type:
	`count =0` We defined a new variable **count**
	`While:True` and then press enter and press the tab key
- Everything which is indented with tab under this line will now be repeated. To stop a running program you can click on the trashcan icon on the terminal window
- With the `count` variable we can make the pi count for us and by combining it with the `print()` we can get it to tell us how many time it has counted!
	- On the new line write: `count = count +1` This will increase the count variable by one.
	- On the next line under write: `print(count)`. Now try running the code!
	- Look at how fast it counts! Maybe a bit too fast... Click on the trashcan icon in the terminal window.
### Libraries and counting seconds
Let's slow the program down a bit, so that it counts seconds instead. To do that we will use the **time** library ( a library is a pre-written set of code). This will allow us to use special pre-written commands.

- At the top of the file: Write `import time # Import the Time library`
	- Congratulations! You have now imported your first library and written a comment with the # symbol. Comments are notes about the code which is ignored by the computer and are helpful to explain what your code does!
- Let's now add a new line under `print(count)`: 
	- Write `time.sleep(1)` which will make the program wait 1 second
	- Try running the code! The program should now display the count and wait 1 second and then loop back to count again!
<br>
<br>
<br> <br>
### Functions and if-statements
What if we only wanted to print count when the number is even? How can we make the program know when an number is even or not? To do that, we will define our very own command instead called a function. It's a block of code that performs a specific task. Imagine you're baking cookies – instead of writing out the recipe every time you want to bake, you create a recipe (function) with instructions for baking cookies, and whenever you want cookies, you just use that recipe.
- At the top of the file, under `import time` write the following code:
```python
def isEven(count): 
# If count is even, return True, if it is uneven return False
	if (count % 2) == 0:
		return True
	else:
		return False
```
- The first line defines the name of our function and what variables (if any) it can receive. In our case, we want it to receive **count**. 
- The second line is called an if-statement, which is an incredibly useful tool that allows you to execute code if a certain expression is **True**.  The expression in the parenthesis uses the modulo operator (the % sign) on count and 2, which will give zero for even numbers and 1 for uneven ones. The double equals signs is an operator which allows us to tell python to compare two numbers and tell us if they are equal (which will give **True** if they are equal, or **False** if they are not equal).  There are many other ways to compare numbers, just like in math you can use less than(<), greater than (>), less than or equal (**<=**) and greater than or equal (**>=**).
- The next line occurs if our statement turns out out to be true. the `return` statement in Python is used inside a function to send back a result or value to the part of the program that called the function. In this case we want to return **True**.
- The `else:` line tells python what to do if the if statement turned out to be false, in this case that would mean that **count** is uneven. In that case, we want to return **False**. 
Let's also change our while-loop:
rewrite the while command and everything under it so it looks like this:
```python
While True:
	count= count+1 
	if isEven(count):
		print(count)
	time.sleep(1)
```
- In the if-statement, we call our function `isEven` and  if it returns True, python will print **count**
- Try running the code now! It should just print even numbers!
<br>
<br>
<br>
## Controlling your robot
Now that you have gained a basic understanding of python, let us try out the robot. In this part you will learn how to make the robot go forwards, backwards, turn left and turn right. You will also learn how to use the distance sensor as well as how to control the speed of the robot. You will be given step-by step instructions, and tasks to complete and a final task involving making the robot avoid obstacles!

### Task 1: Controlling the motors
- Make a new file in Vs code: Click on "file" in the upper corner -> "new file". Then write "Motors.py" and press ENTER. Save the file on the desktop.
- In the file we will import the time library again and a new library called the GPIOZero library,  and from it we will import the `CamJamKitRobot` object. Write the following code and make sure you understand what it does:  
```python 
import time  # Import the Time library
from gpiozero import CamJamKitRobot #Import the GPIO Zero CamJam library
robot = CamJamKitRobot() # Start the robot
# Turn the motors on
robot.forward()
# Go forwards for 1 second
time.sleep(1)
# Turn the motors off
robot.stop() 
```
 - The third line will start our robot
 - robot.forward() will  turn the motors on and make the robot go forward, we then use the time.sleep(1) command to make it go forwards
 - robot.stop() will turn off the motors and make the robot stop. 
 - Now try it out! It should start going forward for 1 second. 

### Task 2: driving and turning
- Congrats, you made the robot go forwards. Now lets try to make it turn and go backwards.
- In the same file, under the time.sleep() command, write the following code:
```python
robot.backward() # Go backwards
time.sleep(1) # Go backwards for 1 second
robot.left()     # Turn left
time.sleep(0.5)  # Turn left for half a second
robot.right()  # Turn right
time.sleep(0.5) # Turn right for half a second
```
- Now try running the code! The robot should first go forward for 1 second, then backwards and finally turn left for 0,5 second and then turn right for 0,5 second. 
<br> 
### Task 3: calibrating the speed
You may have noticed that the robot will go relatively fast, let's try to slow it down. Edit your code so that it looks like this:
```python
import time  # Import the Time library
from gpiozero import CamJamKitRobot #Import the GPIO Zero Library CamJam library
robot = CamJamKitRobot() # Start the robot
speed = 0.3 # Set the relative speed of the motors between 0.0-1.0
robot.forward(speed) # Turn the motors on
time.sleep(1) # Go forwards for 1 second
robot.backward(speed) # Go backwards
time.sleep(1) # Go backwards for 1 second
robot.left(speed)     # Turn left
time.sleep(0.5)  # Turn left for half a second
robot.right(speed)  # Turn right
time.sleep(0.5) # Turn right for half a second
robot.stop() #Turn the motor off
```
- We have made a new variable called **speed** which we will use to set the speed of the motors. In all commands which make the robot move we have added **speed** in the parentheses, which will make the robots move at the specified speed. Try running the code now. It should go slower. Try changing the speed too!
	
### Task 4: Using the distance sensor
Now that you have used the motors for a bit, let's try using the ultrasonic distance sensor. But before then, we will explain how the sensor works. When voltage is applied to the **Trig pin** on the sensor, it sends a ultrasonic sound from its speaker which is then recived from its reciever when the sound travels back. The calculated distance is then sent from the **echo pin**. Write the following code to test the sensor in a new file and name it "Distance.py":
```python
import time #Import the Time library
from gpiozero import DistanceSensor #Import GPIO Zero Library
# Define GPIO pins to use on the Pi
pintrigger = 17
pinecho = 18
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger) # Start the sensor object
print("Ultrasonic Measurement")
try:
	  # Repeat the next indented block forever
	  while True:
		  distance= sensor.distance *100 
		  print(distance) # Sensor measures in meters, multiply 100 to get cm
# If you press CTRL+C, the program will stop
except KeyboardInterrupt:
	  exit()
```
- Import DistanceSensor allows us to use the distance sensor.
- the **pintrigger** and **pinecho** variables define which pins on the motorcontroller are used for the sensor.
- the line after that will start our sensor, with our specified pins. 
- The **try** and **except** lines will make it possible to stop the program with CTRL+C. Dont worry if you dont fully understand. 
- In the while loop, we assign the variable **distance** the measured distance from the sensor and the print it using print()
- Now try running the file! To test that the sensor gives correct and different readings, try putting your hand in front of the sensor at various distances. 
### Task 5:  Obstacle Avoidance Robot
You have now learned everything you need to make your own obstacle avoidance robot! You will be given some code beforehand to help you start out, but the final result is up to you! Edit the file so that it looks like this: 

```python
import time  # Import the Time library
from gpiozero import CamJamKitRobot, DistanceSensor  # Import GPIO Zero Libraries
# Define GPIO pins to use for the distance sensor
pintrigger = 17
pinecho = 18
robot = CamJamKitRobot()
sensor = DistanceSensor(echo=pinecho, trigger=pintrigger)
# Variables for you to use, maybe you want to define some more?
hownear = 0  # How near should the robot be before doing something?
speed= 0 # How fast should the robot be going?
def isnearobstacle(localhownear):
# We want the function to tell us if the robot is near an object or not 
    distance = sensor.distance * 100 # Sensor measures in meters, multiply 100 to get cm
    print("IsNearObstacle: " + str(distance))    
def avoidobstacle():
    # Define here what the robot should do when it is near an object
    # What should it do to avoid an obstacle?
    print("Backwards")
try:
    # repeat the next indented block forever
    while True:
        robot.forward(speed)
        time.sleep(0.1)
        if isnearobstacle(hownear): 
        # If the robot is near an obstacle, how close should it be before doing something?
            robot.stop()
            avoidobstacle()
# If you press CTRL+C, cleanup and stop
except KeyboardInterrupt:
    robot.stop()
```
- The current code is incomplete, it will just continue forwards and ignore any objects in its path.
- It is up to you to define the two functions **isnearobstacle()** and **avoidobstacle()**. Good luck! 
