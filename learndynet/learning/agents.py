from learnDyNet.learndynet.learning.learning import Learning


class Agents (Learning):
    def __init__(self,config):
        super(Agents,self).__init__(config)
        self.__agentDic={}

    def initAgents(self,state):
        pass


    class Agent:
        def __init__(self,edge):
            self.__edge=edge
            self.__cost=0
            self.state=""




