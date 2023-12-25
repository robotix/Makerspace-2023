import curses
from gpiozero import Motor

class Robot:
    def __init__(self, motors):
        self.front_motor = Motor(forward = motors[0], backward = motors[1])
        self.right_motor = Motor(forward = motors[2], backward = motors[3])
        self.left_motor = Motor(forward = motors[4], backward = motors[5])
        self.back_motor = Motor(forward = motors[6], backward = motors[7])

    def forward(self):

    def backward(self):

    def right(self):

    def left(self):

    def clock(self):

    def anticlock(self):
        

actions = {
    curses.KEY_UP:    robot.forward,
    curses.KEY_DOWN:  robot.backward,
    curses.KEY_LEFT:  robot.left,
    curses.KEY_RIGHT: robot.right,
}

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
