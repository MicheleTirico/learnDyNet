import random


class Individuals:
    def __init__(self,config,network):
        self.__config=config
        self.__network=network
        self.__individuals={}

    def initIndividuals(self):
        if self.__config.typeInitIndividuals=="random": self.__initIndividualsRandom(self.__config.multipleIndividualsOverVertex)

    def getIndividuals(self):       return self.__individuals
    def getIndividual(self,id):     return self.__individuals[id]
    def __initIndividualsRandom(self,multipleIndividualsOverVertex):
        G=self.__network.getGraph()
        p=self.__config.percentIndividuals
        i=0
        nodes=list(G.nodes)
        list_pos_assigned=[]
        while i < int(len(G.nodes)*p):
            node_pos=random.randrange(0,len(nodes))
            if multipleIndividualsOverVertex==False:
                if node_pos not in list_pos_assigned:
                    list_pos_assigned.append(node_pos)
                    node=nodes[node_pos]
                    test=False
                    activityPos=None
                    while test==False:
                        activityPos=random.randrange(0,len(nodes))
                        if activityPos != node_pos: test=True
                    activityNode=nodes[activityPos]
                    individual=Individual(i)
                    individual.setStartPos(node)
                    individual.setActivity(activityNode)
                    self.__individuals[i]=individual
            else:
                node=nodes[node_pos]
                test=False
                activityPos=None
                while test==False:
                    activityPos=random.randrange(0,len(nodes))
                    if activityPos != node_pos: test=True
                activityNode=nodes[activityPos]
                individual=Individual(i)
                individual.setStartPos(node)
                individual.setActivity(activityNode)
                self.__individuals[i]=individual
            i+=1

class Individual:
    def __init__(self,id):
        self.__id=id
        self.__startPos=0
        self.__activityPos=0
        self.__sp=[]
        self.__utilities=[]

    def setStartPos(self,startPos):     self.__startPos=startPos
    def setActivity(self,activityPos):  self.__activityPos=activityPos
    def getStartPos(self):              return self.__startPos
    def getActivityPos(self):           return self.__activityPos

    def getSp(self):                    return self.__sp
    def getUtilities(self):             return  self.__utilities
    def setSp(self,sp):                 self.__sp=sp
    def setUtilities(self,utilities):   self.__utilities=utilities
