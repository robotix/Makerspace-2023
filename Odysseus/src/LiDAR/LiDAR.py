import os
import time
from logging import INFO, FileHandler, Formatter, getLogger

import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from serial import Serial


class LiDAR:
    """
    LiDAR class
    """

    def __init__(self, port, baudrate, timeout):
        self.ser = Serial(port, baudrate, timeout=timeout)
        self.ser.flush()

    def __del__(self):
        self.ser.close()

    def getScan(self):
        self.ser.write(b"g")
        data = self.ser.readline().decode("utf-8")
        data = data.split(",")
        data = [int(i) for i in data]
        return data

    def visualize(self):
        fig = plt.figure()
        ax = fig.add_subplot(1, 1, 1)
        xs = np.arange(0, 360)
        ys = [0] * 360
        (line,) = ax.plot(xs, ys)
        ax.set_ylim(0, 1000)
        ax.set_xlim(0, 360)
        ax.set_autoscale_on(False)
        while True:
            data = self.getScan()
            line.set_ydata(data)
            fig.canvas.draw()
            fig.canvas.flush_events()
            time.sleep(0.01)


if __name__ == "__main__":
    logger = getLogger(__name__)
    logger.setLevel(INFO)

    if not os.path.exists("../../logs"):
        os.makedirs("../../logs")

    fileHandler = FileHandler("../../logs/info.log")
    fileHandler.setLevel(INFO)

    formatter = Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s")

    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    logger.info("LiDAR.py is running as main")

    # lidar = LiDAR('/dev/ttyUSB0', 115200, 1)
    # lidar.visualize()
