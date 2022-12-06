import networkx as nx
import networkx.exception

from learnDyNet.learndynet.mobility.discreteModeChoice import DiscreteModeChoice


class Mobility():
    def __init__(self,config,network,individuals):
        self.__config=config
        self.__network=network
        self.__individuals=individuals

    def initMobility(self):

        if self.__config.typeMobilityModel=="discreteModeChoice":
            dmc=DiscreteModeChoice(self.__config,self.__network,self.__individuals)

    def compute(self,step):
        G_sim=self.__network.getGraphSim(step)
        for id , individual in self.__individuals.getIndividuals().items():
            try:
                sp_walk_go=nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
                sp_walk_back=nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
                utility_walk_go=nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
                utility_walk_back=nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
            except networkx.exception.NetworkXNoPath:
                sp_walk_go=[]
                sp_walk_back=[]
                utility_walk_go=-10
                utility_walk_back=-10
            try:
                sp_bike_go=nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
                sp_bike_back=nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
                utility_bike_go=nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
                utility_bike_back=nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
            except networkx.exception.NetworkXNoPath:
                sp_bike_go=[]
                sp_bike_back=[]
                utility_bike_go=-10
                utility_bike_back=-10
            try:
                sp_car_go=nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")
                sp_car_back=nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")
                utility_car_go=nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")
                utility_car_back=nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")
            except networkx.exception.NetworkXNoPath:
                sp_car_go=[]
                sp_car_back=[]
                utility_car_go=-10
                utility_car_back=-10

            sp_walk=[sp_walk_go,sp_walk_back]
            utility_walk=[round(utility_walk_go,3),round(utility_walk_back,3)]

            sp_bike=[sp_bike_go,sp_bike_back]
            utility_bike=[round(utility_bike_go,3),round(utility_bike_back,3)]

            sp_car=[sp_car_go,sp_car_back]
            utility_car=[round(utility_car_go,3),round(utility_car_back,3)]

            individual.setSp([sp_walk,sp_bike,sp_car])
            individual.setUtilities([utility_walk,utility_bike,utility_car])

            #    print(sp_walk,sp_bike,sp_car,sep="\n")
            #    print(utility_walk,utility_bike,utility_car,sep="\n")
            """

            sp_walk_go=nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
            sp_bike_go=nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
            sp_car_go=nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")

            utility_walk_go=nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
            utility_bike_go=nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
            utility_car_go=nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")

            sp_walk_back=nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
            sp_bike_back=nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
            sp_car_back=nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")

            utility_walk_back=nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
            utility_bike_back=nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
            utility_car_back=nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")

            sp_walk=[sp_walk_go,sp_walk_back]
            utility_walk=[utility_walk_go,utility_walk_back]

            sp_bike=[sp_bike_go,sp_bike_back]
            utility_bike=[utility_bike_go,utility_bike_back]

            sp_car=[sp_car_go,sp_car_back]
            utility_car=[utility_car_go,utility_car_back]

            individual.setSp([sp_walk,sp_bike,sp_car])
            individual.setUtilities([utility_walk,utility_bike,utility_car])

            """