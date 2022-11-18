from learnDyNet.learndynet.network.network import Network
from networkx import grid_graph, grid_2d_graph
import networkx as nx

class NetworkGrid (Network):
    def __init__(self,config,network):
        super (NetworkGrid,self).__init__(config)
        self.__config=config
        self.__network=network

    def initNetwork(self):
        print (self.__config.graph_grid_dimension_x)
        gridGraph=grid_graph(dim=(self.__config.graph_grid_dimension_x,self.__config.graph_grid_dimension_y))
        pos={}
        i=0
        for x in range(0,self.__config.graph_grid_dimension_x):
            for y in range(0,self.__config.graph_grid_dimension_y):
                pos[i]=(x*self.__config.graph_grid_dist_x,y*self.__config.graph_grid_dist_y)
                i+=1
        nx.set_node_attributes(gridGraph,pos,"coord")

        for e in gridGraph.edges:
            a=nx.get_edge_attributes(gridGraph,e)
            print (e[0])
            print (a)

        self.__network.setGraph(gridGraph)

    def __getDist (self,G,n1,n2):
        pos1=nx.get_node_attributes(G,"coord")
        print (pos1)