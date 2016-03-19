
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

        self.stepDt = 15
        self.drawDt = 15

        self.conflict = ConflictManager()
        self.clock = SimClock(0)

    def start(self):
        print("Starting kernel...")

        root = Tk()
        self.tk = root
        self.canvas = EnvironmentView(self.tk, self.clock)

        # schedule update function
        root.after(self.stepDt, self.step)
        root.mainloop()




    def step(self):
        logging.info("Rendering...")
        self.canvas.clear()
        self.agm.draw(self.canvas)
        self.canvas.draw_clock()

        logging.info("Spawning new Agents...")
        #TODO

        logging.info("Updating Agents...")
        self.agm.update(self.stepDt)

        logging.info("Resolving Conflicts...")
        actions = self.agm.collect_actions()
        final_actions = self.conflict.resolve(actions)
        self.agm.clear_actions()

        logging.info("Performing Actions...")
        self.agm.perform_actions(final_actions)

        self.clock._addTime(self.stepDt)

        self.tk.after(self.stepDt, self.step)  # reschedule update function
