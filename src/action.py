


class Action:

    def __init__(self, agent_id, action_type, action):
        self.agent_id = agent_id
        self.action_type = action_type
        self.action = action


    def __str__(self):
        return "A:%s, T:%s - %s;"%(self.agent_id, self.action_type, self.action)
