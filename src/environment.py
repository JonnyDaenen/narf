

class Environment:

    avatars = {}

    def __init__(self, width, height):
        self.width = width
        self.height = height


    def add_avatar(self, agent_id, avatar):
        avatars[agent_id] = avatar
