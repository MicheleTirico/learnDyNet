

class QLearning:
    def __init__(self,config,network,agents):
        self.__config=config
        self.__network=network
        self.__agents=agents

    def computeLearning(self,step):

        for id, agent in self.__agents.getAgents().items():
            print (id, agent.getMap())










