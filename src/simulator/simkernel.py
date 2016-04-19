import logging
from tkinter import *

from simulator.agent.agentmanager import AgentManager
from simulator.environment.conflictmanager import ConflictManager
from simulator.environment.environment import Environment
from simulator.environment.environmentview import EnvironmentView
from simulator.kernel.kernelclock import KernelClock
from simulator.services.servicemanager import ServiceManager
from simulator.services.whitepages import WhitePages


class SimKernel:

    _stepDt = 30 # milliseconds between frames
    _prev = 0 # timestamp op prev frame
    #_drawDt = 15

    _servicemanager = None

    def __init__(self):
        logging.info("Loading Kernel...")

        self._clock = KernelClock(0)
        self._prev = self._clock.get_currenttime()

        self.create_servicemanager()

        logging.info("Kernel loaded...")


    def create_servicemanager(self):
        logging.info("Loading Servicemanager modules...")
        servicemanager = ServiceManager()

        logging.debug("Adding whitepage service...")
        servicemanager.register_service("WHITEPAGES", WhitePages())

        logging.debug("Adding enviroment service...")
        servicemanager.register_service("ENVIRONMENT", Environment(800,600))
        # servicemanager.register_service("CLOCK", ..())
        # servicemanager.register_service("GPS", ..())
        # servicemanager.register_service("SPAWNER", ..())

        self._servicemanager = servicemanager

    def start(self):

        logging.info("Creating canvas...")
        root = Tk()
        self.tk = root
        self.canvas = EnvironmentView(self.tk, self._clock)

        # schedule update function
        root.after(self._stepDt, self.step)
        logging.info("Starting kernel...")
        root.mainloop()

    def check_delta(self):
        """
        Checks whether the elapsed time between prev and current call was
        significantly higher than _stepDt. If so, a warning is printed.
        """
        curr = self._clock.get_currenttime()
        delta = curr - self._prev
        delta /= 1000
        if delta > self._stepDt + 5:
            logging.warning("Too large delta: %s"%delta)
        self._prev = curr

    def next_step(self):
        """
        Measure the time elapsed between the _prev timestamp set at the
        beginning of the frame and now. This is deducted from _stepDt
        in order to obtain the sleep time before the next frame.
        """
        curr = self._clock.get_currenttime()
        delta = curr - self._prev
        delta /= 1000
        delta = max(0, int(delta)) # no negative delta

        return self._stepDt - delta

    def step(self):

        # print warning when kernel is too slow
        self.check_delta()

        logging.debug("Refreshing Environment...")
        self.refresh_enviroment()

        logging.debug("Spawning new Agents...") # TODO implement module
        self.spawn_agents()

        logging.debug("Updating Agents...")
        self.update_agents()

        logging.debug("Updating Environment...")
        self.update_environment()

        # TODO decouple rendering from update
        logging.debug("Rendering...")
        self.render()

        logging.debug("Updating clock for next frame...")
        self._clock.add_step(self._stepDt)


        # reschedule update function
        step = self.next_step()
        self.tk.after(step, self.step)

    def spawn_agents(self):
        pass

    def update_agents(self):
        pass

    def update_environment(self):
        pass

    def render(self):
        self.canvas.clear()
        self.canvas.draw_clock()

    def refresh_enviroment(self):
        pass
