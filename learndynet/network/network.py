import networkx as nx
import matplotlib.pyplot as plt

class Network ():

    def __init__(self,config,stateSet):
        self.__config=config
        self.__stateSet=stateSet
        self.__agents=0
        self.__G=0 # network
        self.__G_sim={}
        self.__stateSet=stateSet

    def setAgents(self,agents): self.__agents=agents
    def setStateSet(self,stateSet): self.__stateSet=stateSet

    def getGraph (self):         return self.__G
    def setGraph (self,graph):   self.__G=graph
    def getGraphSim(self,step):     return self.__G_sim[step]

    def dispayGraph(self,run):
        if run:
            nx.draw(self.__G)
            plt.show()

    def displayGraphSimInfo(self,step):
        print ("--------- graph sim info ------------")
        print ("n edges =",len(self.__G_sim[step].edges))
        print (self.__G_sim[step].edges)
        print ("-------------------------------------")

    def createNetwork(self,step):
        G_sim=nx.MultiDiGraph()
        G_sim.add_nodes_from(self.__G)
        for id in self.__agents.getAgents():
            agent=self.__agents.getAgents()[id]
        #    print (step-1,agent,agent.getStates())
            state=agent.getState(step)
        #    print ("agent",id,state,agent.getStates())
            vertices=agent.getVertices()
            length=agent.getLength()

            for ed in state:
                mode,dir,cost=ed[0],ed[1],float(ed[2])
                if dir=='from-to':  v0,v1=vertices[0],vertices[1]
                else:               v0,v1=vertices[1],vertices[0]
                noWeightVal=self.__config.length_out
                weight_walk,weight_bike,weight_car=noWeightVal,noWeightVal,noWeightVal
                if      mode=="walk":   weight_walk=cost*length
                elif    mode=="bike":   weight_bike=cost*length
                else:                   weight_car=cost*length
#                print (ed,length,dir,cost,weight_walk,weight_bike,weight_car)
                G_sim.add_edge(v0,v1,length=length,weight_walk=weight_walk,weight_bike=weight_bike,weight_car=weight_car)# mode=mode,cost=cost,weight=cost*length

        self.__G_sim[step]=G_sim
        # quit()
