from datetime import datetime

class KernelClock:

    def __init__(self, initialtime=0, initialstep=0):
        self._time = initialtime
        self._laststep = initialstep


    def add_step(self, step):
        self._time += step
        self._laststep = step


    def get_time(self):
        return self._time


    def get_laststep(self):
        return self._laststep


    def get_currenttime(self):
        dt = datetime.now()
        return dt.microsecond