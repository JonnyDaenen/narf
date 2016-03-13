
import random

class Agent:

    def __init__(self, id):
        self.id = id

        self.pos = [0,0]
        self.speed = 30
        # create normalized direction vector
        vect = [random.random()*2-1,random.random()*2-1]
        size = (vect[0]**2 + vect[1]**2)**0.5
        self.direction = [vect[0]/size, vect[1]/size]


        # self.actions = []


    def update(self,stepDt):

        # calculate update vector
        s = stepDt/1000
        f = self.speed * s
        update_vect = [f * p for p in self.direction]

        # update position
        print(stepDt, update_vect, s)
        self.pos = list(map(sum, zip(self.pos,update_vect)))


    def __str__(self):
        return "Agent %s @%s v%s s%s"%(self.id, self.pos, self.direction, self.speed)


    def add_action(self,action):
        # self.actions.append(action)
        pass
