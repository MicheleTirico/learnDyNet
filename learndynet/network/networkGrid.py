from learnDyNet.learndynet.network.network import Network
from networkx import grid_graph
import networkx as nx

class NetworkGrid (Network):
    def __init__(self,config,network):
        super (NetworkGrid,self).__init__(config)
        self.__config=config
        self.__network=network

    def initNetwork(self):
        self.__G=grid_graph(dim=(self.__config.graph_grid_dimension_x,self.__config.graph_grid_dimension_y))
        pos={}
        i=0
        for x in range(0,self.__config.graph_grid_dimension_x):
            for y in range(0,self.__config.graph_grid_dimension_y):
                pos[i]=(x*self.__config.graph_grid_dist_x,y*self.__config.graph_grid_dist_y)
                i+=1
        nx.set_node_attributes(self.__G,pos,"coord")
        nx.set_node_attributes(self.__G,list(range(0,self.__config.graph_grid_dimension_x*self.__config.graph_grid_dimension_y)),"id")

        i=0
        for e in self.__G.edges:
            self.__G.edges[e[0],e[1]]["id"]=i
            i+=1
        self.__network.setGraph_states(self.__G)

    def __getDist (self,G,n1,n2):
        pos1=nx.get_node_attributes(G,"coord")
        print (pos1)

    def getGridNetwork (self):         return self.__G