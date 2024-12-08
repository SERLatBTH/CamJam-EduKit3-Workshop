import time
from gpiozero import CamJamKitRobot, DistanceSensor

INSTRUCTION_DELAY = 0.5 # seconds

class Robot:
    def __init__(self):
        self._robot = CamJamKitRobot()
        self._mirror = False
        self._sensor = None
        try:
            self._sensor = DistanceSensor(echo=18, trigger=17)
        except:
            print("Distance sensor not found!")

        self.go = self.Go(self)
        self.rotate = self.Rotate(self)
        self.see = self.See(self)

    class Go:
        def __init__(self, parent):
            self.parent = parent

        def forward(self, power=100, duration=None):
            if power < 0 or power > 100:
                print("Power must be between 0 and 100! Skipping instruction...")
                return
            power = power/100
            message = "Moving forward"
            message += f" for {duration} seconds" if duration is not None else ""
            print(message)
            self.parent._robot.forward(power)
            if duration is None:
                return
            time.sleep(duration)
            self.parent._robot.stop()
            time.sleep(INSTRUCTION_DELAY)
            return
        
        def backward(self, power=100, duration=None):
            if power < 0 or power > 100:
                print("Power must be between 0 and 100! Skipping instruction...")
                return
            power = power/100
            message = "Moving backward"
            message += f" for {duration} seconds" if duration is not None else ""
            print(message)
            self.parent._robot.backward(power)
            if duration is None:
                return
            time.sleep(duration)
            self.parent._robot.stop()
            time.sleep(INSTRUCTION_DELAY)
            return
        
    class Rotate:
        def __init__(self, parent):
            self.parent = parent

        def left(self, power=100, duration=None):
            if power < 0 or power > 100:
                print("Power must be between 0 and 100! Skipping instruction...")
                return
            power = power/100
            message = "Turning left"
            message += f" for {duration} seconds" if duration is not None else ""
            print(message)
            self.parent._robot.left(power) if not self.parent._mirror else self.parent._robot.right(power)
            if duration is None:
                return
            time.sleep(duration)
            self.parent._robot.stop()
            time.sleep(INSTRUCTION_DELAY)
            return
        
        def right(self, power=100, duration=None):
            if power < 0 or power > 100:
                print("Power must be between 0 and 100! Skipping instruction...")
                return
            power = power/100
            message = "Turning right"
            message += f" for {duration} seconds" if duration is not None else ""
            print(message)
            self.parent._robot.right(power) if not self.parent._mirror else self.parent._robot.left(power)
            if duration is None:
                return
            time.sleep(duration)
            self.parent._robot.stop()
            time.sleep(INSTRUCTION_DELAY)
            return

    class See:
        def __init__(self, parent):
            self.parent = parent

        def distance(self):
            if self.parent._sensor is None:
                return None
            distance = round(self.parent._sensor.distance * 100, 1)
            if distance >= 100:
                print("I don't detect anything in front of me...")
                return None
            print(f"I detect something {distance} cm away")
            return distance
        
    def pause(self, duration=1):
        print(f"Pausing for {duration} seconds")
        self._robot.stop()
        time.sleep(duration)
        return
    
    def mirror(self, active=None):
        if active is not None:
            self._mirror = active
        else:
            self._mirror = not self._mirror
        print(f"Mirror mode is {self._mirror}")
        return
