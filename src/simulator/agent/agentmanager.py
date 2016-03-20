
from simulator.agent.agent import Agent

class AgentManager:

    def __init__(self):
        self.agentMap = {}
        self.nextID = 0
        pass

    def createAgent(self):
        id = self.nextID
        self.nextID += 1
        self.agentMap[id] = Agent(id)

    def update(self,stepDt):
        for id, agent in self.agentMap.items():
            agent.update(stepDt)

    def collect_actions(self):
        actions = []
        for id, agent in self.agentMap.items():
            actions += agent.get_actions()

        return actions

    def clear_actions(self):
        for id, agent in self.agentMap.items():
            agent.clear_actions()

    def perform_actions(self, actions):
        for action in actions:
            self.agentMap[action.agent_id].perform_action(action)


    def draw(self, canvas):
        for id, agent in self.agentMap.items():
            canvas.draw_agent(agent)

    def __str__(self):
        s = ""
        for id, agent in self.agentMap.items():
            s += str(agent) + "\n"
        return s
