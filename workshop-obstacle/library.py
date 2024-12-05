import time
from gpiozero import CamJamKitRobot, DistanceSensor

_robot = CamJamKitRobot()
_sensor = DistanceSensor(echo=18, trigger=17)

_mirror = False
def mirror(active=None):
    global _mirror
    if active is not None:
        _mirror = active
    else:
        _mirror = not _mirror
    print(f"Mirror mode is {_mirror}")

def reportImpact(lowest):
    distance = round(_sensor.distance * 100, 1)
    if lowest < distance:
        return lowest
    if distance < 10 and lowest > 10:
        print("I hit something!")
    elif distance < 25 and lowest > 25:
        print("I'm getting close to something")
    elif distance < 60 and lowest > 60:
        print("I see something")
    return distance


def forward(power=100, duration=None, distance=None):
    if power < 0 or power > 100:
        print("Power must be between 0 and 100! Skipping instruction...")
        return
    power = power/100
    start = time.time()
    print(f"Moving forward for {duration} seconds")
    _robot.forward(power)
    lowestDistance = round(_sensor.distance * 100, 1)
    while time.time() - start < duration or duration is None:
        time.sleep(0.04)
        lowestDistance = reportImpact(lowestDistance)
        if distance is not None and lowestDistance <= distance:
            break
        pass
    _robot.stop()
    return

def backward(power=100, duration=None):
    if power < 0 or power > 100:
        print("Power must be between 0 and 100! Skipping instruction...")
        return
    power = power/100
    if duration is not None:
        print(f"Moving backward for {duration} seconds")
        _robot.backward(power)
        time.sleep(duration)
        _robot.stop()
        return
    print("Moving backward")
    _robot.backward(power)

def left(power=100, duration=None):
    if power < 0 or power > 100:
        print("Power must be between 0 and 100! Skipping instruction...")
        return
    power = power/100
    if duration is not None:
        print(f"Turning left for {duration} seconds")
        if _mirror:
            _robot.right(power)
            print("Turning right through mirror")
        else:
            _robot.left(power)
            print("Turning left")

        
        print(f"Mirror mode is {_mirror}")
        time.sleep(duration)
        _robot.stop()
        return
    print("Turning left")
    if _mirror:
        _robot.right(power)
    else:
        _robot.left(power)

def right(power=100, duration=None):
    if power < 0 or power > 100:
        print("Power must be between 0 and 100! Skipping instruction...")
        return
    power = power/100
    if duration is not None:
        print(f"Turning right for {duration} seconds")
        if _mirror:
            _robot.left(power)
        else:
            _robot.right(power)
        time.sleep(duration)
        _robot.stop()
        return
    print("Turning right")
    if _mirror:
        _robot.left(power)
    else:
        _robot.right(power)

def stop(duration=None):
    if duration is not None:
        print(f"Stopping for {duration} seconds")
        _robot.stop()
        time.sleep(duration)
        return
    print("Stopping")
    _robot.stop()

def distance():
    distance = round(_sensor.distance * 100, 1)
    if distance >= 100:
        print("I don't detect anything in front of me...")
        return None
    print(f"I detect something {distance} cm away")
    return distance
