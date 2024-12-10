# Robot Obstacle Course Workshop

[Ändra till svenska](instructions-sv.md)

Today we're going to code a robot to navigate through an obstacle course.

Coding is like giving your robot a set of instructions to follow. We'll be using three panels to do this:

- **Left Panel: The Code File.** This is where you'll write your instructions for the robot.
- **Bottom Panel: Chat Box with the Robot.** Here, you'll send commands to the robot.
- **Right Panel: Cheat Sheet.** This has all the information you need.

## Robot Chat Box

We'll use the chat to send our code to the robot. The robot will read your instructions and follow them.

To send your code to the robot, type this in the chat:

```plaintext
runonrobot code.py
```

If the robot keeps going and you need it to stop, press `CTRL+C` on your keyboard to make it stop right away.

## Instructions

Here are all the commands you can give the robot:

- `power`: How strong the robot moves (from 0% to 100%).
- `duration`: How long the robot should perform the action (in seconds). Remember, use a `.` for decimal points in code.

```python
robot.go.forward(power=80, duration=1.4)

robot.go.backward(power=80, duration=1.4)

robot.rotate.left(power=50, duration=0.2)

robot.rotate.right(power=50, duration=0.1)

robot.pause(duration=1)

robot.see.distance() # The robot will tell you how far it is from something
```

# Your Task

### 1. Make the robot go forward. 
- What happens when you do this?
### 2. Make the robot rotate left. 
- Does it rotate to the left?
- (If it does, set `mirror(False)` to `True`)
### 3. Make the robot rotate 90 degrees.
- Are there any problems rotating 90 degrees to the left?
- Same problems rotating right?
### 4. Go through the maze and knockout the rat kings from their throne!