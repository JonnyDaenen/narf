


class WhitePages:

    def __init__(self):
        self.agent_to_id = {}
        self.id_to_agent = {}
        self.next_id = 1


    def lookup_by_id(self, id):
        return self.id_to_agent[id]

    def lookup_by_agent(self, agent):
        return self.agent_to_id[agent]

    def register_agent(self, agent):
        id = self.next_id
        self.id_to_agent[id] = agent
        self.agent_to_id[agent] = id

        self.next_id += 1
        return id

    def get_avatar(self, agent):
        pass