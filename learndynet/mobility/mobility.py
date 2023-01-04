import networkx as nx
import networkx.exception

from learnDyNet.learndynet.mobility.discreteModeChoice import DiscreteModeChoice


class Mobility():
    def __init__(self,config,network,individuals):
        self.__config=config
        self.__network=network
        self.__individuals=individuals
        self.__numberTripNotFunded=[]

    def initMobility(self):

        if self.__config.typeMobilityModel=="discreteModeChoice":
            dmc=DiscreteModeChoice(self.__config,self.__network,self.__individuals)

    def compute(self,step):
        numberTripNotFunded=0
        G_sim=self.__network.getGraphSim(step)
        for id , individual in self.__individuals.getIndividuals().items():
            length_go_back=[]
            sp_go_back=[]
            weigths=["weight_walk","weight_bike","weight_car"]
            for w in weigths:
                # go trip
                try:
                    sp_go=          nx.shortest_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight=w)
                    length_go=      nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight=w)
                    if length_go>0 and length_go<self.__config.length_out:
                        sp_go_back.append(sp_go)
                        length_go_back.append(length_go)
                    else:
                        sp_go_back.append([])
                        length_go_back.append(0)
                except nx.exception.NetworkXNoPath:
                    sp_go_back.append([])
                    length_go_back.append(0)
                # came back trip
                try:
                    sp_back=        nx.shortest_path(G_sim,target=individual.getStartPos(),source=individual.getActivityPos(),weight=w)
                    length_back=    nx.shortest_path_length(G=G_sim,target=individual.getStartPos(),source=individual.getActivityPos(),weight=w)
                    if length_back>0 and length_back<self.__config.length_out:
                        sp_go_back.append(sp_back)
                        length_go_back.append(length_back)
                    else:
                        sp_go_back.append([])
                        length_go_back.append(0)
                except nx.exception.NetworkXNoPath:
                    sp_go_back.append([])
                    length_go_back.append(0)

            sp_walk=[sp_go_back[0],sp_go_back[1]]
            sp_bike=[sp_go_back[2],sp_go_back[3]]
            sp_car=[sp_go_back[4],sp_go_back[5]]
            utility_walk,utility_bike,utility_car=[0,0],[0,0],[0,0]
            utility=[utility_walk,utility_bike,utility_car]
            for u in range(0,3):
                u1,u2,t=0.0,0.0,False
                if length_go_back[u*2] !=0:    u1=round(self.__config.alpha_m[u] + ( individual.getTheta()[u] +1 ) / length_go_back[u*2],3)
                else:
                    u1=self.__config.rewardNoTripFunded
                    t=True
                if length_go_back[u*2+1] !=0:    u2=round(self.__config.alpha_m[u] + ( individual.getTheta()[u] +1 ) / length_go_back[u*2+1],3)
                else:
                    u2=self.__config.rewardNoTripFunded
                    t=True

                if t==True:
                    numberTripNotFunded+=1
                utility[u]=[u1,u2]
            """
            print ("-----------------------",id)
            print (G_sim.edges)
            print ("walk",sp_walk)
            print ("bike",sp_bike)
            print ("car",sp_car)
            print ("lengths",length_go_back)
            print ("utility",utility)
            """
            individual.setSp([sp_walk,sp_bike,sp_car])
            individual.setUtilities([utility[0],utility[1],utility[2]])

        self.__numberTripNotFunded.append(numberTripNotFunded)

    def compute_old_01(self,step):
        numberTripNotFunded=0
        G_sim=self.__network.getGraphSim(step)
        for id , individual in self.__individuals.getIndividuals().items():
            length_go_back=[]
            try:
                sp_walk_go=         nx.shortest_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk",method="bellman-ford")
                sp_walk_back=       nx.shortest_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
                length_walk_go=     nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_walk")
                length_walk_back=   nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_walk")
                if length_walk_go>0 and length_walk_go<1000: # set 1000
                    length_go_back.append(round(length_walk_go,3))
                else:
                    sp_walk_go=[]
                    length_walk_go=self.__config.rewardNoTripFunded
            except networkx.exception.NetworkXNoPath:
                sp_walk_go=[]
                sp_walk_back=[]
                length_walk_go=self.__config.rewardNoTripFunded
                length_walk_back=self.__config.rewardNoTripFunded
            length_go_back.append(round(length_walk_go,3))
            length_go_back.append(round(length_walk_back,3))
            try:
                sp_bike_go=nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
                sp_bike_back=nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
                length_bike_go=nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_bike")
                length_bike_back=nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_bike")
            except networkx.exception.NetworkXNoPath:
                sp_bike_go=[]
                sp_bike_back=[]
                length_bike_go=self.__config.rewardNoTripFunded
                length_bike_back=self.__config.rewardNoTripFunded

            length_go_back.append(round(length_bike_go,3))
            length_go_back.append(round(length_bike_back,3))

            try:
                sp_car_go       =nx.dijkstra_path(G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")
                sp_car_back     =nx.dijkstra_path(G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")
                length_car_go   =nx.shortest_path_length(G=G_sim,source=individual.getStartPos(),target=individual.getActivityPos(),weight="weight_car")
                length_car_back =nx.shortest_path_length(G=G_sim,source=individual.getActivityPos(),target=individual.getStartPos(),weight="weight_car")
            except networkx.exception.NetworkXNoPath:
                sp_car_go=[]
                sp_car_back=[]
                length_car_go=self.__config.rewardNoTripFunded
                length_car_back=self.__config.rewardNoTripFunded

            length_go_back.append(round(length_car_go,3))
            length_go_back.append(round(length_car_back,3))

            sp_walk=[sp_walk_go,sp_walk_back]
            sp_bike=[sp_bike_go,sp_bike_back]
            sp_car=[sp_car_go,sp_car_back]
            utility_walk,utility_bike,utility_car=[0,0],[0,0],[0,0]
            utility=[utility_walk,utility_bike,utility_car]
            for u in range(0,3):
                u1,u2,t=0.0,0.0,False
                if length_go_back[u*2] !=0:    u1=round(self.__config.alpha_m[u] + ( individual.getTheta()[u] +1 ) / length_go_back[u*2],3)
                else:
                    u1=self.__config.rewardNoTripFunded
                    t=True
                if length_go_back[u*2+1] !=0:    u2=round(self.__config.alpha_m[u] + ( individual.getTheta()[u] +1 ) / length_go_back[u*2+1],3)
                else:
                    u2=self.__config.rewardNoTripFunded
                    t=True

                if t==True:numberTripNotFunded+=1

                utility[u]=[u1,u2]
            print ("-----------------------",id)
            print (G_sim.edges)
            print ("walk",sp_walk)
            print ("bike",sp_bike)
            print ("car",sp_car)
            print ("lengths",length_go_back)
            print ("utility",utility)

            individual.setSp([sp_walk,sp_bike,sp_car])
            individual.setUtilities([utility[0],utility[1],utility[2]])

        self.__numberTripNotFunded.append(numberTripNotFunded)

    def getNumberTripNotFunded(self):           return self.__numberTripNotFunded
