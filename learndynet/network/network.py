import networkx as nx
import matplotlib.pyplot as plt

class Network ():

    def __init__(self,config):
        self.__config=config
        self.__G_states=0 # network states
        self.__G_sim=nx.empty_graph(0,default=nx.DiGraph)
        self.__stateSet=0

    def setStateSet(self,stateSet): self.__stateSet=stateSet
    def init_G_sim(self):
        self.__G_sim.add_nodes_from(self.__G_states)

    def update_G_sim(self):
        print("update")
        print(len(self.__G_sim.nodes),len(self.__G_sim.edges))
        for e in self.__G_states.edges:
            print(e,self.__G_states.get_edge_data(e[0],e[1]))
            states=self.__G_states.get_edge_data(e[0],e[1])["states"]
            state_name=states[len(states)-1]
            print (states,type(states))
            state=self.__stateSet.getState(state_name)
            print (type(state))
            self.__G_sim.add_edge(e[0])


    def getGraph_states (self):         return self.__G_states
    def setGraph_states (self,graph):   self.__G_states=graph

    def dispayGraph_states(self,run):
        if run:
            nx.draw(self.__G_states)
            plt.show()

    def dispayGraph_sim(self,run):
        if run:
            nx.draw(self.__G_sim)
            plt.show()
