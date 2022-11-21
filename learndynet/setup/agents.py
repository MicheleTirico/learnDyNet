import networkx as nx


class Agents:
    def __init__(self,config,network,stateSet):
        self.__config=config
        self.__network=network
        self.__stateSet=stateSet
        self.__agents={}

    def initAgents(self):
        if self.__config.initStateMode=="same": self.__initStatesSame()

    def __initStatesSame(self):
        self.__G=self.__network.getGraph_states()
        state=self.__stateSet.getState(self.__config.initState)
    #    nx.set_edge_attributes(self.__G,state.getName(),"state")
        nx.set_edge_attributes(self.__G,[state.getName()],"states")
        nx.set_edge_attributes(self.__G,[0],"qvalue")
        for e in self.__G.edges:
            id=self.__G.get_edge_data(e[0],e[1])["id"]
            agent=Agent(id)
            agent.appendQvalue(0)
            agent.appendState(state)
            # .....
            self.__agents[id]=agent

class Agent:
    def __init__(self,name):
        self.__name=name
        self.__states=[]
        self.__qtab=[]
        self.__state=""
        self.__qvalue=0
        self.__qvalues=[]
    # TODO: add all other values, init qtab

    def setQvalue(self,qvalue): self.__qvalue=qvalue
    def setState(self,state): self.__state=state
    def setStates(self,pos,state): self.__states[pos]=state
    def appendState(self,state):    self.__states.append(state)
    def appendQvalue(self,qvalue):  self.__qvalues.append(qvalue)