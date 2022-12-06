import random
from numpy.random import RandomState
import numpy as np

class Learning():
    def __init__(self,config,network,stateSet,actionSet,agents):
        self.__config=config
        self.__network=network
        self.__stateSet=stateSet
        self.__actionSet=actionSet
        self.__agents=agents
        self.__rdSelectAction=np.random.RandomState(3)
#        self.__rdAction=    np.random.RandomState(self.__config.seedRandomAction)
#     self.__rdState=     np.random.RandomState(self.__config.seedRandomState)
 #       self.__rdMode=      np.random.RandomState(self.__config.seedRandomMode)
  #      self.__rdDirection= np.random.RandomState(self.__config.seedRandomDirection)

    # def setSeed(self,seed):   random.seed(seed)
    def computeLearning(self,step):
        if    self.__config.typelearning=="qlearning":        self.__computeQlearning(step)

    def selectActions(self,step):
        if self.__config.actionModeSelection=="random":     self.__selectActionRandom(step)
        elif self.__config.actionModeSelection=="greedy":   self.__selectActionGreedy(step)

    def __selectActionRandom(self,step):
        print ("select action random")
        for id in self.__agents.getAgents():
            agent=self.__agents.getAgents()[id]
            state=agent.getStates()[step-1]
            statePos=self.__stateSet.getStatePos(state)
            allowedActions=self.__stateSet.getAllowedActions(state)
            actionPos=allowedActions[self.__rdSelectAction.randint(len(allowedActions))]
            action=self.__actionSet.getActions()[actionPos]
            newState=self.__stateSet.getStateFromAction(state,action)
            agent.appendState(newState)
            agent.appendAction(action)

            print ("----------- agent",id)
            print ("states before:",agent.getStates())
            print ("state at step ",step-1,":",state)
            print ("position of state:",statePos)
            print ("allowedActions",allowedActions)
            print ("random action position:",actionPos)
            print ("random action:",action)
            print ("newState:",newState)
            print ("states after:",agent.getStates())

    def __selectActionGreedy(self,step):
        print ("select action greedy")
        for id in self.__agents.getAgents():
            agent=self.__agents.getAgents()[id]
            state=agent.getStates()[step-1]
            statePos=self.__stateSet.getStatePos(state)
            allowedActions=self.__stateSet.getAllowedActions(state)
            actionPos=self.__getActionGreedy(step,allowedActions,agent,statePos)
            action=self.__actionSet.getActions()[actionPos]
            newState=self.__stateSet.getStateFromAction(state,action)
            agent.appendState(newState)
            agent.appendAction(action)

    def __getActionGreedy(self, step,allowedActions ,agent,statePos):
        epsilonMin=self.__config.epsilonmin
        nSim=self.__config.numStep
        epsilon = max(epsilonMin, 1 - step / nSim)
        if random.uniform(0, 1) < epsilon:                  actionPos=allowedActions[self.__rdSelectAction.randint(len(allowedActions))]
        else:
#            listActions=list(agent.getQtabMap()[step-1][statePos])
            listActions=list(agent.getQtabList()[step-1][statePos])

            maxVal = max(listActions)
            posMax = listActions.index(maxVal)
            actionPos=self.__actionSet.getActions().index(self.__actionSet.getActions()[posMax])
            if actionPos not in allowedActions:             actionPos=allowedActions[self.__rdSelectAction.randint(len(allowedActions))]
        return actionPos

    def __computeQlearning(self, step):
    #    print ("ciao q learning ")
        for id in self.__agents.getAgents():
            agent=self.__agents.getAgent(id)
            states=agent.getStates()
            actions=agent.getActions()
            state=states[step]
            action=actions[step-1]
            statePos=self.__stateSet.getStatePos(state)
            actionPos=self.__actionSet.getActionPos(action)
            old_qVal=agent.getQtabList()[step-1][statePos][actionPos]
#            old_qVal=agent.getQtab()[step-1,statePos,actionPos]
            alpha=self.__config.learning_alpha
            reward=agent.get_reward_pos(step)
            gamma=self.__config.learning_gamma
#            maxVal=max(agent.getQtab()[step-1][statePos])
            maxVal=max(agent.getQtabList()[step-1][statePos])
            new_qVal=old_qVal + alpha * (reward + gamma * maxVal - old_qVal)
#            agent.setQval(step,statePos,actionPos,new_qVal)
            agent.setQtabList(step,statePos,actionPos,new_qVal)





    def getActionRandom(self,state):
        actions=self.__stateSet.getAllowedActions(state)
        return actions[random.randint(0,len(actions)-1)]
