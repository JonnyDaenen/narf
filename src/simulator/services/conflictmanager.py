

class ConflictManager:

    def __init__(self):
        pass


    def resolve(self, actions):

        for action in actions:
            if action.action_type == "pos":
                action.action[0] = action.action[0] % 600
                action.action[1] = action.action[1] % 400

        return actions
