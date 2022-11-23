import networkx as nx

from learnDyNet.learndynet.mobility.discreteModeChoice import DiscreteModeChoice


class Mobility():
    def __init__(self,config,network,individuals):
        self.__config=config
        self.__network=network
        self.__individuals=individuals

    def initMobility(self):

        if self.__config.typeMobilityModel=="discreteModeChoice":
            dmc=DiscreteModeChoice(self.__config,self.__network,self.__individuals)

    def compute(self):
        G=self.__network.getGraph()
        print (self.__individuals.getIndividuals())
        for id , individual in self.__individuals.getIndividuals().items():
#            individual=self.__individuals.getIndividuals.get(id)
            sp_walk=nx.dijkstra_path(self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
            sp_bike=nx.dijkstra_path(self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
            sp_car=nx.dijkstra_path(self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")



            utility_walk=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
            utility_bike=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
            utility_car=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")
            print(utility_walk,utility_bike,utility_car)
            print (id,individual)
            print ("sp_walk",sp_walk)
            print ("sp_bike",sp_bike)
            print ("sp_car",sp_car)
            for node in sp_walk:
                print (node)

            sim_edges = [(u,v) for u,v,e in self.__network.getGraph().edges(data=True) if e["edge_function"] == "sim"]
            G_sim=nx.subgraph(self.__network.getGraph(),sim_edges)
            walk_edges = [(u,v) for u,v,e in self.__network.getGraph().edges(data=True) if e["modes"] == "walk"]

            quit()
            walk_edges= [(u,v) for u,v,e in self.__network.getGraph().edges(data=True) if e["modes"] == "walk"]
            list_ed=self.__network.getGraph().edges(sp_car[0],sp_car[1])
            for n,values in self.__network.getGraph().adj[sp_car[0]][sp_car[1]].items():
                attrib=self.__network.getGraph().adj[sp_car[0]][sp_car[1]].get(n)
                if attrib["edge_function"]=="state":print (n)


            quit()
