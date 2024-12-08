import library
robot = library.Robot()

robot.mirror(True) # Ändra till 'False' för att spegelvända robotens rotationer

robot.go.forward(power=50, duration=2)
robot.rotate.left(power=50, duration=0.1)
robot.go.forward(70, 2)
robot.rotate.left(50, 0.1)
robot.go.backward(50, 1)
robot.pause(1)
robot.rotate.right(80, 1000)


