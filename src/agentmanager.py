
from agent import Agent

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


    def draw(self, canvas):
        for id, agent in self.agentMap.items():
            canvas.draw_agent(agent)


    def __str__(self):
        s = ""
        for id, agent in self.agentMap.items():
            s += str(agent) + "\n"
        return s
