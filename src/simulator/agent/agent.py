import random

from simulator.actions.action import Action


class Agent:

    def __init__(self, id):
        self.id = id

        self.pos = [0,0]
        self.speed = 30
        # create normalized direction vector
        vect = [random.random()*2-1,random.random()*2-1]
        size = (vect[0]**2 + vect[1]**2)**0.5
        self.direction = [vect[0]/size, vect[1]/size]

        # action indications
        self.actions = []


    def update(self,stepDt):

        # calculate update vector
        s = stepDt/1000
        f = self.speed * s
        update_vect = [f * p for p in self.direction]

        # update position
        # print(stepDt, update_vect, s)
        newpos = list(map(sum, zip(self.get_pos(),update_vect)))

        self.move_to(newpos)

    def perform_action(self, action):
        if action.type == "pos":
            self.pos = action.action


    def __str__(self):
        return "Agent %s @%s v%s s%s"%(self.id, self.pos, self.direction, self.speed)


    ## action functions

    def emit_action(self, action):
        self.actions.append(action)

    def get_actions(self):
        return self.actions

    def clear_actions(self):
        self.actions = []


    ## position functions

    def move_to(self, pos):
        action = Action(self.id, "pos", pos)
        self.emit_action(action)

    def get_pos(self):
        return self.pos
