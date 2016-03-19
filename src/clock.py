

from datetime import datetime

class SimClock:

    def __init__(self, initial_time):
        self.time = initial_time
        self.lastDelta = 0

    def _addTime(self, delta):
        self.time += delta
        self.lastDelta = delta

    def get_time(self):
        return self.time

    def lastdelta(self):
        return self.lastdelta


    def get_currenttime(self):
        dt = datetime.now()
        return dt.microsecond
