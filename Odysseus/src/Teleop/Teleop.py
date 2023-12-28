import curses
from gpiozero import Motor

class robot:
    def __init__(self, motors):
        self.front_motor = Motor(forward = motors[0], backward = motors[1])
        self.right_motor = Motor(forward = motors[2], backward = motors[3])
        self.left_motor = Motor(forward = motors[4], backward = motors[5])
        self.back_motor = Motor(forward = motors[6], backward = motors[7])
        print("Robot is initialized")

    def forward(self):
        self.front_motor.stop()
        self.right_motor.forward()
        self.left_motor.forward()
        self.back_motor.stop()
        print("Moving forward")

    def backward(self):
        self.front_motor.stop()
        self.right_motor.backward()
        self.left_motor.backward()
        self.back_motor.stop()
        print("Moving backward")

    def right(self):
        self.front_motor.forward()
        self.right_motor.stop()
        self.left_motor.stop()
        self.back_motor.forward()
        print("Moving right")

    def left(self):
        self.front_motor.backward()
        self.right_motor.stop()
        self.left_motor.stop()
        self.back_motor.backward()
        print("Moving left")

    def anticlock(self):
        self.front_motor.backward()
        self.left_motor.backward()
        self.back_motor.forward()
        self.right_motor.forward()
        print("Turning anti-clockwise")

    def clock(self):
        self.front_motor.forward()
        self.left_motor.forward()
        self.back_motor.backward()
        self.right_motor.backward()
        print("Turning clockwise")

    def stop(self):
        self.front_motor.stop()
        self.left_motor.stop()
        self.back_motor.stop()
        self.right_motor.stop()
        print("Robot has stopped moving")
        

actions = {
    curses.W:   robot.forward,
    curses.S:   robot.backward,
    curses.A:   robot.left,
    curses.D:   robot.right,
    curses.Q:   robot.anticlock,
    curses.E:   robot.clock
}

motors = [17, 18, 23, 24, 22, 27, 5, 6]

def main(window):
    next_key = None
    while True:
        curses.halfdelay(1)
        if next_key is None:
            key = window.getch()
        else:
            key = next_key
            next_key = None
        if key != -1:
            # KEY PRESSED
            curses.halfdelay(3)
            action = actions.get(key)
            if action is not None:
                action()
            next_key = key
            while next_key == key:
                next_key = window.getch()
            # KEY RELEASED
            robot.stop()

curses.wrapper(main)
