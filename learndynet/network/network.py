import networkx as nx
import matplotlib.pyplot as plt

class Network ():

    def __init__(self,config):
        self.__config=config
        self.__G=0

    def getGraph (self):    return self.__G
    def setGraph (self,graph):    self.__G=graph

    def dispayGraph(self):
        nx.draw(self.__G)
        plt.show()