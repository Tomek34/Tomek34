import random

class Sensor:
    def __init__(self):
        self.temperature = 0
        self.humidity = 0
        self.pressure = 0

    def read_data(self):
        self.temperature = random.uniform(10, 30)
        self.humidity = random.uniform(30, 80)
        self.pressure = random.uniform(990, 1030)