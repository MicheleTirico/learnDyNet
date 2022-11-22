import math

import networkx as nx
import numpy as np


class Agents:
    def __init__(self,config,network,stateSet):
        self.__config=config
        self.__network=network
        self.__stateSet=stateSet
        self.__agents={}

    def initAgents(self):
        if self.__config.initStateMode=="same": self.__initStatesSame()

    def __initStatesSame(self):
        self.__G=self.__network.getGraph()
        state=self.__stateSet.getState(self.__config.initState)
        state_name=state.getName()
        lines=state.getLines()
        edges=list(self.__G.edges)

        # set attributes for edge state
        qtab=np.zeros(shape=(self.__stateSet.getNstates(),self.__stateSet.getNstates()))
        nx.set_edge_attributes(self.__G,qtab,"qtab")
        nx.set_edge_attributes(self.__G,"state","edge_function")
        nx.set_edge_attributes(self.__G,[state_name],"state")
        # create edge sim and add attrib
        id_sim=0
        for e in edges:

            length=self.__G.edges[e]["length"]
            for line in lines:
                for nLines in range(0,int(line[1])):
                    if line[3]=="from-to":
                        self.__G.add_edge(e[0],e[1],id_sim=id_sim,modes=line[0],cost=line[2],edge_function="sim",length=length)
                    else:
                        self.__G.add_edge(e[1],e[0],id_sim=id_sim,modes=line[0],cost=line[2],edge_function="sim",length=length)
                    id_sim+=1



#            if self.__G.get_edge_data(e)"edge_funtion"]=="sim": print (e)
"""
    #    nx.set_edge_attributes(self.__G,state.getName(),"state")
        nx.set_edge_attributes(self.__G,[state.getName()],"states")
        nx.set_edge_attributes(self.__G,[0],"qvalue")
        for e in self.__G.edges:
            id=self.__G.get_edge_data(e[0],e[1])["id"]
            agent=Agent(id)
            agent.appendQvalue(0)
            agent.appendState(state)
            agent.setNodes([e[0],e[1]])
            # .....
            self.__agents[id]=agent
"""
class Agent:
    def __init__(self,name):
        self.__name=name
        self.__states=[]
        self.__qtab=[]
        self.__state=""
        self.__qvalue=0
        self.__qvalues=[]
        self.__nodes=[]

    # TODO: add all other values, init qtab
    def setNodes(self,nodes):           self.__nodes=nodes
    def setQvalue(self,qvalue):         self.__qvalue=qvalue
    def setState(self,state):           self.__state=state
    def setStates(self,pos,state):      self.__states[pos]=state
    def appendState(self,state):        self.__states.append(state)
    def appendQvalue(self,qvalue):      self.__qvalues.append(qvalue)