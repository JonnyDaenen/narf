
from tkinter import Canvas
import logging

class EnvironmentView():


    def __init__(self, tk, clock):
        self.width = 600
        self.height = 400
        self.clock = clock

        # create canvas
        w = Canvas(tk, width=self.width, height=self.height)
        w.pack()
        self.canvas = w

        # cache
        self.cache = {}


    def transform(self, pos):
        # return (pos[0] + self.width/2, pos[1] + self.height/2)
        return pos

    def clear(self):
        # TODO it is not necessary to delete everything, we can just update it
        # self.canvas.delete("all")
        pass

    def draw_clock(self):
        clock_id = "clock"
        time = str(self.clock.get_time()//1000)
        if clock_id in self.cache:
            self.canvas.itemconfig(self.cache[clock_id], text=time)
        else:
            canvas_id = self.canvas.create_text(10, 10, anchor="nw")
            self.canvas.itemconfig(canvas_id, text=time)
            self.cache[clock_id] = (canvas_id)


    def draw_agent(self, agent):
        pos = agent.pos
        pos = self.transform(pos)
        x = pos[0]
        y = pos[1]
        r = 10
        self.draw_circle(agent.id, x, y, r, agent.direction, agent.speed)


    def draw_circle(self, id, x, y, r, v, s):
        length = r
        if id in self.cache:
            logging.debug("cache update")
            self.canvas.coords(self.cache[id][0],x, y, x+v[0]*length, y+v[1]*length)
            self.canvas.coords(self.cache[id][1],x-r, y-r, x+r, y+r)
        else:
            circle_id = self.canvas.create_oval(x-r, y-r, x+r, y+r, fill="#ff9900", outline="#CC6600" )
            line_id = self.canvas.create_line(x, y, x+v[0]*length, y+v[1]*length, fill="#CC6600")
            self.cache[id] = (line_id, circle_id)
