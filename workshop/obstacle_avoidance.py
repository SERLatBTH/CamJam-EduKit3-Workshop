import time
from gpiozero import CamJamKitRobot, DistanceSensor

robot = CamJamKitRobot()
sensor = DistanceSensor(echo=18, trigger=17)
speed = 1.0
detect_distance = 10

while True:
    robot.forward(speed)
    print(sensor.distance)
    time.sleep(1)
    if sensor.distance * 100 < detect_distance:
        robot.stop()
        robot.backward(speed)
        time.sleep(1)
        robot.left(speed)
        time.sleep(speed)