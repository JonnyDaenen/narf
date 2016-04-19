from simulator.actions.action import Action


class Avatar:

    _speed = 0
    _pos = [0, 0]
    _direction = [1, 1]
    _viewangle = 360
    _viewradius = 50

    _actions = []

    def __init__(self, x, y):
        self._pos = [x,y]


    # update

    def do_step(self,stepDt):

        # calculate update vector
        s = stepDt/1000
        f = self._speed * s
        update_vect = [f * p for p in self._direction]

        # update position
        # print(stepDt, update_vect, s)
        newpos = list(map(sum, zip(self._pos,update_vect)))

        self.move_to(newpos)


    def perform_action(self, action):
        if action.type == "pos":
            self.pos = action.action


    def __str__(self):
        return "Avatar %s @%s v%s s%s"%(self.id, self.pos, self.direction, self.speed)


    ## action functions

    def emit_action(self, action):
        self._actions.append(action)

    def get_actions(self):
        return self._actions

    def clear_actions(self):
        self._actions = []


    ## position functions

    def move_to(self, pos):
        action = Action(self.id, "pos", pos)
        self.emit_action(action)

    def get_pos(self):
        return self.pos