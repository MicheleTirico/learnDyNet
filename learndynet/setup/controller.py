import os
import sys


class Controller:

    def __init__ (self,config,learning,network,mobility,reward):
        self.__config=config
        self.__learning=learning
        self.__network=network
        self.__mobility=mobility
        self.__reward=reward

        self.__config.logger.log(cl=self,method=sys._getframe(),message="initialize controller")

    def initSimulation(self):
        paths=[self.__config.pathTmp,self.__config.pathOutputs,self.__config.pathOutput]
        self.__initFolder(paths)


    def __initFolder (self,paths):
        for path in paths :
            self.__config.logger.log(cl=self,method=sys._getframe(),message="create folder in: "+path)
            os.system("mkdir "+path)


    def run (self):
        print ("\n------------------------ start simulation ------------------------------------\n")
        step =1
        while step < self.__config.numStep:
            print ("------------------------- step", step,"---------------------------------------------")
            #network.displayGraphSimInfo(step-1)

            # select actions
            self.__learning.selectActions(step)

            # create network
            print ("create network")
            self.__network.createNetwork(step)
            #   network.displayGraphSimInfo(step)

            # mobility
            print ("compute mobility")
            self.__mobility.compute(step)

            # reward
            print ("compute reward")
            self.__reward.computeReward(step)
            #   reward.displayRewards()

            # compute learning
            print ("compute learning")
            self.__learning.computeLearning(step)
            #    print ("states =",len(stateSet.getStateSet()),stateSet.getStateSet())

            step+=1

