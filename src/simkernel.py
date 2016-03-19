
import time
import logging

from agentmanager import AgentManager
from conflictmanager import ConflictManager
from environmentview import EnvironmentView
from tkinter import *
from clock import SimClock


class SimKernel:

    def __init__(self):
        print("kernel loaded")
        self.agm = AgentManager()
        for i in range(100):
            self.agm.createAgent()

        self.conflict = ConflictManager()
        self.clock = SimClock(0)

        self.stepDt = 15
        self.drawDt = 15
        self.prev = self.clock.get_currenttime()

    def start(self):
        print("Starting kernel...")

        root = Tk()
        self.tk = root
        self.canvas = EnvironmentView(self.tk, self.clock)

        # schedule update function
        root.after(self.stepDt, self.step)
        root.mainloop()


    def check_delta(self):
        curr = self.clock.get_currenttime()
        delta = curr - self.prev
        delta /= 1000
        if delta > self.stepDt + 5:
            logging.warning("Too large delta: %s"%delta)
        self.prev = curr

    def next_step(self):
        curr = self.clock.get_currenttime()
        delta = curr - self.prev
        delta /= 1000
        delta = max(0,int(delta))

        return self.stepDt - delta

    def step(self):

        self.check_delta()

        logging.info("Rendering...")
        self.canvas.clear()
        self.agm.draw(self.canvas)
        self.canvas.draw_clock()

        logging.info("Spawning new Agents...")
        #TODO implement module

        logging.info("Updating Agents...")
        self.agm.update(self.stepDt) # TODO provide actual time step

        logging.info("Resolving Conflicts...")
        actions = self.agm.collect_actions()
        final_actions = self.conflict.resolve(actions)
        self.agm.clear_actions()

        logging.info("Performing Actions...")
        self.agm.perform_actions(final_actions)

        self.clock._addTime(self.stepDt)

        step = self.next_step()

        self.tk.after(step, self.step)  # reschedule update function
