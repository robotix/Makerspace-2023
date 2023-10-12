from gpiozero import Motor
from time import sleep
from logging import getLogger, FileHandler, Formatter, INFO
import os

class Motors:
    def __init__(self, leftMotor, rightMotor, frontMotor, backMotor):
        self.leftMotor = Motor(leftMotor[0], leftMotor[1])
        self.rightMotor = Motor(rightMotor[0], rightMotor[1])
        self.frontMotor = Motor(frontMotor[0], frontMotor[1])
        self.backMotor = Motor(backMotor[0], backMotor[1])

    def forward(self, speed):
        self.leftMotor.forward(speed)
        self.rightMotor.backward(speed)
    
    def backward(self, speed):
        self.leftMotor.backward(speed)
        self.rightMotor.forward(speed)

    def right(self, speed):
        self.frontMotor.forward(speed)
        self.backMotor.backward(speed)

    def left(self, speed):
        self.frontMotor.backward(speed)
        self.backMotor.forward(speed)

    def clockwise(self, speed):
        self.leftMotor.forward(speed)
        self.rightMotor.forward(speed)
        self.frontMotor.forward(speed)
        self.backMotor.forward(speed)

    def counterClockwise(self, speed):
        self.leftMotor.backward(speed)
        self.rightMotor.backward(speed)
        self.frontMotor.backward(speed)
        self.backMotor.backward(speed)

    def stop(self):
        self.leftMotor.stop()
        self.rightMotor.stop()
        self.frontMotor.stop()
        self.backMotor.stop()

    def test(self):
        self.forward(0.5)
        sleep(1)
        self.backward(0.5)
        sleep(1)
        self.right(0.5)
        sleep(1)
        self.left(0.5)
        sleep(1)
        self.clockwise(0.5)
        sleep(1)
        self.counterClockwise(0.5)
        sleep(1)
        self.stop()

if __name__ == "__main__":
    logger = getLogger(__name__)
    logger.setLevel(INFO)

    if not os.path.exists('../../logs'):
        os.makedirs('../../logs')
    
    fileHandler = FileHandler('../../logs/info.log')
    fileHandler.setLevel(INFO)

    formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.info("Motors.py is running as main")

    # motors = Motors([17, 18], [22, 23], [24, 25], [5, 6])
    # motors.test()




