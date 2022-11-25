
import math

import networkx as nx
import numpy as np


class Agents:
    def __init__(self,config,network,stateSet):
        self.__config=config
        self.__network=network
        self.__stateSet=stateSet
        self.__agents={}
        self.__G= self.__network.getGraph()

    def initAgents(self):
        for edge in self.__G.edges(data=True):
            fun= edge[2]["edge_function"]
            id=edge[2]["id"]

            if fun=="state":
                state=edge[2]["state"]
                agent=Agent(id)
                agent.setStates(0,state) # is the same of agent.appendState(state)
                agent.setListStates(self.__stateSet.getListStates())
                self.__agents[(edge[0],edge[1])]=agent

    def getAgent(self,edge_0,edge_1):
        try:    return self.__agents[(edge_0,edge_1)]
        except KeyError:
            return self.__agents[(edge_1,edge_0)]
    def getAgents(self):     return self.__agents

    def updateReward(self,step):
        for id , agent in self.__agents.items():
            num_ind=agent.get_num_ind_pos(step)
            sum_utility=agent.get_sum_utility_pos(step)
            agent.append_reward(round(sum_utility/num_ind,3))

class Agent:
    def __init__(self,id):
        self.__id=id
        self.__states=[]
        self.__num_ind=[0]
        self.__sum_utility=[0]
        self.__reward=[]
        self.__listStates=[]
        self.__qTab=np.zeros(shape=(len(self.__listStates),len(self.__listStates)))

    def getMap(self):   return {"id":self.__id,"states":self.__states,"num_ind":self.__num_ind,"sum_utility":self.__sum_utility,"reward":self.__reward}

    # TODO: add all other values, init qtab
    def setStates(self,pos,state):
        if len(self.__states)==0: self.appendState(state)
        else:        self.__states[pos]=state
    def appendState(self,state):        self.__states.append(state)
    def getStates(self):            return self.__states

    def set_num_ind(self,pos,num_ind):
        if len(self.__num_ind)==0: self.append_num_ind(num_ind)
        else:        self.__num_ind[pos]=num_ind
    def append_num_ind(self,num_ind):        self.__num_ind.append(num_ind)

    def set_sum_utility(self,pos,sum_utility):
        if len(self.__sum_utility)==0: self.append_sum_utility(sum_utility)
        else:        self.__sum_utility[pos]=sum_utility
    def append_sum_utility(self,sum_utility):        self.__sum_utility.append(sum_utility)

    def set_reward(self,pos,reward):
        if len(self.__reward)==0: self.append_reward(reward)
        else:        self.__reward[pos]=reward
    def append_reward(self,reward):        self.__reward.append(reward)

    def get_sum_utility(self):        return self.__sum_utility
    def get_num_ind(self):        return self.__num_ind
    def get_reward(self):        return self.__reward

    def get_num_ind_pos(self,pos):
        try: return self.__num_ind[pos]
        except IndexError:
            self.__num_ind.append(0)
            return self.__num_ind[pos]
    def get_sum_utility_pos(self,pos):
        try: return self.__sum_utility[pos]
        except IndexError:
            self.__sum_utility.append(0)
            return self.__sum_utility[pos]
    def get_reward_pos(self,pos):
        try: return self.__reward[pos]
        except IndexError:
            self.__reward.append(0)
            return self.__reward[pos]

    def setListStates(self, listStates):    self.__listStates=listStates

