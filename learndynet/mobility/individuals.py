import random

import numpy as np

from learnDyNet.learndynet.utils import utils


class Individuals:
    def __init__(self,config,network):
        self.__config=config
        self.__network=network
        self.__individuals={}
        self.__combinationsAlpha=[]

    def initIndividuals(self):
        self.__rd_theta=np.random.RandomState(self.__config.seed_setup_theta)

        if self.__config.setupInitPositionIndividuals=="random":self.__initIndividualsRandom()

    def getIndividuals(self):       return self.__individuals
    def getIndividual(self,id):     return self.__individuals[id]
    def __initIndividualsRandom(self):
        G=self.__network.getGraph()
        p=self.__config.percentIndividuals
        i=0
        nodes=list(G.nodes)
        list_pos_assigned=[]
        if self.__config.setup_theta_m=="random":  combinations_theta=utils.getCombinationsList(self.__config.theta_m)
        while i < int(len(G.nodes)*p):
            node_pos=random.randrange(0,len(nodes))
            node=0
            activityNode=0
            individual=Individual(i)

            if self.__config.multipleIndividualsOverVertex==False:
                if node_pos not in list_pos_assigned:
                    list_pos_assigned.append(node_pos)
                    node=nodes[node_pos]
                    test=False
                    activityPos=None
                    while test==False:
                        activityPos=random.randrange(0,len(nodes))
                        if activityPos != node_pos: test=True
                    activityNode=nodes[activityPos]
            else:
                node=nodes[node_pos]
                test=False
                activityPos=None
                while test==False:
                    activityPos=random.randrange(0,len(nodes))
                    if activityPos != node_pos: test=True
                activityNode=nodes[activityPos]

            # setup individuals
            individual.setStartPos(node)
            individual.setActivity(activityNode)

            list_theta=[]
            # set random theta
            if self.__config.setup_theta_m=="random":
                combinations=utils.getCombinationsList(self.__config.theta_m)
                list_theta=combinations[self.__rd_theta.randint(0,len(combinations))]
            elif self.__config.setup_theta_m=="same":
                list_theta=self.__config.theta_m
            else:
                print ("ERROR")
                quit()
            individual.setTheta(list_theta)
            self.__individuals[i]=individual
            i+=1

     #   for id,ind in self.__individuals.items():print (ind,ind.getActivityPos())

class Individual:
    def __init__(self,id):
        self.__id=id
        self.__startPos=0
        self.__activityPos=0
        self.__sp=[]
        self.__utilities=[]
        self.__theta=[]
        self.__alpha=[]

    def setTheta(self,theta):           self.__theta=theta
    def getTheta(self):                 return self.__theta
    def setStartPos(self,startPos):     self.__startPos=startPos
    def setActivity(self,activityPos):  self.__activityPos=activityPos
    def getStartPos(self):              return self.__startPos
    def getActivityPos(self):           return self.__activityPos

    def getSp(self):                    return self.__sp
    def getUtilities(self):             return  self.__utilities
    def setSp(self,sp):                 self.__sp=sp
    def setUtilities(self,utilities):   self.__utilities=utilities
