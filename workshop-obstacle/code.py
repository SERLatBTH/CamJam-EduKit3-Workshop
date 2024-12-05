import library as robot

robot.mirror(True)

robot.forward(power=50, duration=2, distance=40)
robot.left(power=50, duration=0.1)
robot.forward(power=50, duration=2, distance=40)
robot.left(power=50, duration=0.1)
robot.forward(power=50, duration=2, distance=40)
robot.stop(duration=0.6)

robot.backward(power=40, duration=0.6)
robot.right(power=70, duration=0.1)
robot.forward(power=70, duration=2)
robot.right(power=100, duration=0.1)
robot.forward(power=100, duration=0.2)
robot.right(power=100, duration=1000)
robot.stop(duration=0.6)
