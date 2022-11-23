import math

import numpy as np

from learnDyNet.learndynet.network.network import Network
from networkx import grid_graph, MultiDiGraph
import networkx as nx

class NetworkGrid (Network):
    def __init__(self,config,network,stateSet):
        super (NetworkGrid,self).__init__(config,stateSet)
        self.__config=config
        self.__network=network
        self.__stateSet=stateSet

    def initNetwork(self):
        G=grid_graph(dim=(self.__config.graph_grid_dimension_x,self.__config.graph_grid_dimension_y))

        # create list of pos
        pos={}
        i=1
        for x in range(0,self.__config.graph_grid_dimension_x):
            for y in range(0,self.__config.graph_grid_dimension_y):
                pos[i]=(x*self.__config.graph_grid_dist_x,y*self.__config.graph_grid_dist_y)
                i+=1

        # set coord nodes
        i=1
        for node in G.nodes:
            G.nodes[node]["id"]=i
            G.nodes[node]["coord"]=pos.get(i)
            i+=1

        # set id and length edges
        i=1
        for e in G.edges(data=True):
            G.edges[e[0],e[1]]["id"]=i
            coord0=G.nodes[e[0]]["coord"]
            coord1=G.nodes[e[1]]["coord"]
            dist=math.sqrt( math.pow(coord1[0]-coord0[0],2)+math.pow(coord1[1]-coord0[1],2))
            G.edges[e[0],e[1]]["length"]=dist
            i+=1

        self.__G=MultiDiGraph(G)
        for e in self.__G.edges: self.__G.remove_edge(e[1],e[0])


    def getGraph (self):         return self.__G