

class Environment:

    width = 100
    height = 100

    avatars = {}
    objects = {}


    def __init__(self, width, height):
        self.width = width
        self.height = height


    def add_avatar(self, agent_id, avatar):
        self.avatars[agent_id] = avatar

    def refresh(self):
        # TODO refresh all avatars
        pass


    def update(self):
        # get all actions from avatars
        # resolve conflicts
        # apply actions
        pass
