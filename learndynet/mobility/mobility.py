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
        #G=self.__network.getGraph()
        for id , individual in self.__individuals.getIndividuals().items():
            sp_walk_go=nx.dijkstra_path(self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
            sp_bike_go=nx.dijkstra_path(self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
            sp_car_go=nx.dijkstra_path(self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")

            utility_walk_go=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
            utility_bike_go=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
            utility_car_go=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")

            sp_walk_back=nx.dijkstra_path(self.__network.getGraph(),source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
            sp_bike_back=nx.dijkstra_path(self.__network.getGraph(),source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
            sp_car_back=nx.dijkstra_path(self.__network.getGraph(),source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")

            utility_walk_back=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
            utility_bike_back=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
            utility_car_back=nx.shortest_path_length(G=self.__network.getGraph(),source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")

            sp_walk=[sp_walk_go,sp_walk_back]
            utility_walk=[utility_walk_go,utility_walk_back]

            sp_bike=[sp_bike_go,sp_bike_back]
            utility_bike=[utility_bike_go,utility_bike_back]

            sp_car=[sp_car_go,sp_car_back]
            utility_car=[utility_car_go,utility_car_back]

            individual.setSp([sp_walk,sp_bike,sp_car])
            individual.setUtilities([utility_walk,utility_bike,utility_car])

            print(sp_walk,sp_bike,sp_car,sep="\n")
            print(utility_walk,utility_bike,utility_car,sep="\n")
            """

            compute shortest path of first part 
            assign the utility and the shortest path for each mode 
            if exception, assign 0
            
            """