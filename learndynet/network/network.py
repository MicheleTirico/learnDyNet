import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
class Network ():

    def __init__(self,config,stateSet):
        self.__config=config
        self.__stateSet=stateSet
        self.__G=0 # network
        self.__stateSet=stateSet

    def setStateSet(self,stateSet): self.__stateSet=stateSet

    def getGraph (self):         return self.__G
    def setGraph (self,graph):   self.__G=graph

    def dispayGraph(self,run):
        if run:
            nx.draw(self.__G)
            plt.show()
    """
    def setWeights(self):
        val_weigth_out=1000000000
        weights={}
        for e in self.__G.edges:
            edge_function=self.__G.edges[e]["edge_function"]
            if edge_function=="sim":
                modes=self.__G.edges[e]["modes"]
                cost=float(self.__G.edges[e]["cost"])
                length=float(self.__G.edges[e]["length"])
                
                
                weight=[val_weigth_out,val_weigth_out,val_weigth_out]
                if "walk" in modes: weight[0]=round(cost*length,3)
                if "bike" in modes: weight[1]=round(cost*length,3)
                if "car"  in modes: weight[2]=round(cost*length,3)
                weights[e]=weight

        nx.set_edge_attributes(self.__G,weights,"weight")
    """

    def setWeights(self):
        weight_walk,weight_bike,weight_car={},{},{}
        for e in self.__G.edges:
            edge_function=self.__G.edges[e]["edge_function"]
            if edge_function=="sim":
                modes=self.__G.edges[e]["modes"]
                cost=float(self.__G.edges[e]["cost"])
                length=float(self.__G.edges[e]["length"])

                weight_walk[e],weight_bike[e],weight_car[e]=self.__config.val_weigth_out,self.__config.val_weigth_out,self.__config.val_weigth_out
                if "walk" in modes:     weight_walk[e]=round(cost*length,3)
                if "bike" in modes:     weight_bike[e]=round(cost*length,3)
                if "car" in modes:     weight_car[e]=round(cost*length,3)

        nx.set_edge_attributes(self.__G,weight_walk,"weight_walk")
        nx.set_edge_attributes(self.__G,weight_bike,"weight_bike")
        nx.set_edge_attributes(self.__G,weight_car,"weight_car")

    def initAgents(self):
        if self.__config.initStateMode=="same": self.__initStatesSame()

    def __initStatesSame(self):
        state=self.__stateSet.getState(self.__config.initState)
        state_name=state.getName()
        lines=state.getLines()
        edges=list(self.__G.edges)

        # set attributes for edge state
        qtab=np.zeros(shape=(self.__stateSet.getNstates(),self.__stateSet.getNstates()))
        nx.set_edge_attributes(self.__G,qtab,"qtab")
        nx.set_edge_attributes(self.__G,"state","edge_function")
        nx.set_edge_attributes(self.__G,[state_name],"state")

        # create edge sim and add attrib
        id_sim=len(self.__G.edges)+1
        for e in edges:
            length=self.__G.edges[e]["length"]
            for line in lines:
                for nLines in range(0,int(line[1])):
                    if line[3]=="from-to":
                        self.__G.add_edge(e[0],e[1],id=id_sim,modes=line[0],cost=line[2],edge_function="sim",length=length)
                    else:
                        self.__G.add_edge(e[1],e[0],id=id_sim,modes=line[0],cost=line[2],edge_function="sim",length=length)
                    id_sim+=1
