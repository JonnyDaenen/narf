
import time
from agentmanager import AgentManager
from environmentview import EnvironmentView
from tkinter import *


class SimKernel:

    def __init__(self):
        print("kernel loaded")
        self.agm = AgentManager()
        self.agm.createAgent()
        self.agm.createAgent()
        self.agm.createAgent()
        self.agm.createAgent()
        self.agm.createAgent()

        self.stepDt = 15

    def start(self):
        print("Starting kernel...")

        root = Tk()
        self.tk = root
        self.canvas = EnvironmentView(self.tk)

        # schedule update function
        root.after(self.stepDt, self.step)
        root.mainloop()




    def step(self):
        print("Rendering...")
        print(self.agm)
        self.canvas.clear()
        self.agm.draw(self.canvas)

        print("Updating...")
        self.agm.update(self.stepDt)

        print("Resolving...")

        self.tk.after(self.stepDt, self.step)  # reschedule update function
