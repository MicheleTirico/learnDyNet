import shutil
import xml.etree.ElementTree as ET
import os
import sys

import numpy as np

from learnDyNet.learndynet.utils import utils
from learnDyNet.learndynet.utils.logger import Logger


class Config:
    def __init__(self,pathConfig):
        self.__tree = 0              # etree
        self.__root = 0              # etree
        self.pathConfig=pathConfig
        # logger
        self.logger=Logger("test")
        self.logger.setDisplay(True,True,True,True)
        self.__initUrl()

    def __initUrl(self):
        self.logger.log(cl=self,method=sys._getframe(),message="initialize config")
        # etree
        self.__tree=ET.parse(self.pathConfig)
        self.__data=self.__tree.getroot()

        # path url
        self.pathAbs=               self.__getVal("urls","url","absPath")+"/"

        self.pathScenarios=self.pathAbs+self.__getVal("urls","url","scenarios")+"/"
        self.pathScenario=self.pathScenarios+self.__getVal("urls","url","scenario")+"/"
        self.pathTmp=self.pathAbs+self.__getVal("urls","url","tmp")
        self.pathOutputs=self.pathAbs+self.__getVal("urls","url","outputs")+"/"
        self.pathOutput=self.pathOutputs+self.__getVal("urls","url","scenario")
        self.pathStates=self.pathScenario+self.__getVal("urls","url","states")

        # parameters simulation
        self.numStep=               int(self.__getVal("simulation","parameter","numStep"))
        self.initStateMode=         self.__getVal("simulation","parameter","initStateMode")
        self.initState=             int(self.__getVal("simulation","parameter","initState"))
        self.seedInitStateMode=     int(self.__getVal("simulation","parameter","seedInitStateMode"))

        # learning
        self.typelearning=          self.__getVal("learning","parameter","typelearning")
        self.randomseed=            self.__getVal("learning","parameter","randomseed")
        self.learning_gamma=        float(self.__getVal("learning","parameter","learning_gamma"))
        self.epsilonmin=            float(self.__getVal("learning","parameter","epsilonmin"))
        self.learning_alpha=        float(self.__getVal("learning","parameter","learning_alpha"))
        self.roundqvalue=           self.__getVal("learning","parameter","roundqvalue")
        self.rewardNoScore=         self.__getVal("learning","parameter","rewardNoScore")
        """
        self.seedRandomAction=      int(self.__getVal("learning","parameter","seedRandomAction"))
        self.seedRandomState=       int(self.__getVal("learning","parameter","seedRandomState"))
        self.seedRandomMode=        int(self.__getVal("learning","parameter","seedRandomMode"))
        self.seedRandomDirection=   int(self.__getVal("learning","parameter","seedRandomDirection"))
        """
        self.rdSelectAction=        int(self.__getVal("learning","parameter","rdSelectAction"))
        self.actionModeSelection=   self.__getVal("learning","parameter","actionModeSelection")
        self.numStates=0
        self.numActions=0

        # mobility parameters
        self.setupInitPositionIndividuals=   self.__getVal("mobility","parameter","setupInitPositionIndividuals")
        self.percentIndividuals=    float(self.__getVal("mobility","parameter","percentIndividuals"))
        self.typeMobilityModel=     self.__getVal('mobility',"parameter","typeMobilityModel")
 #       self.val_weight_out=        float(self.__getVal("mobility","parameter","val_weight_out"))
        self.modes=                 (self.__getVal("mobility","parameter","modes")).split(",")
        self.directions=            (self.__getVal("mobility","parameter","directions")).split(",")
        self.maxNumberOfEdges=      int(self.__getVal("mobility","parameter","maxNumberOfEdges"))
        self.cost=                  (self.__getVal("mobility","parameter","cost")).split(",")
        self.multipleIndividualsOverVertex=bool(self.__getVal("mobility","parameter","multipleIndividualsOverVertex"))
        self.rewardNoTripFunded=    float(self.__getVal("mobility","parameter","rewardNoTripFunded"))
        self.theta_m=               utils.castFloatElementOfList(self.__getVal("mobility","parameter","theta_m").split(","))
        self.alpha_m=               utils.castFloatElementOfList(self.__getVal("mobility","parameter","alpha_m").split(","))
        self.setup_theta_m=         self.__getVal("mobility","parameter","setup_theta_m")
        self.length_out=            float(self.__getVal("mobility","parameter","length_out"))

        # network parameters
        self.typeNetwork=           self.__getValType("network","parameter","typenetwork","val")

        # grid
        self.graph_grid_dimension_x=int(self.__getValType("network","parameter","dimension_x","grid"))
        self.graph_grid_dimension_y=int(self.__getValType("network","parameter","dimension_y","grid"))
        self.graph_grid_dist_x=float(self.__getValType("network","parameter","dist_x","grid"))
        self.graph_grid_dist_y=float(self.__getValType("network","parameter","dist_y","grid"))

        # seeds
        self.seed_setup_theta=       int(self.__getVal("seeds","parameter","seed_setup_theta"))

        # outputs
        self.path_agentsReward=      self.pathOutput+"/"+self.__getVal("outputs","url","agentsReward")


    def __getVal(self,name_root,name_tag,name):
        tag_root=self.__data.find(name_root)
        for e in tag_root.iter(name_tag):
            if e.get("name")==name: return e.text.replace(" ","")

    def __getValType(self,name_root,name_tag,name,type):
        tag_root=self.__data.find(name_root)
        for e in tag_root.iter(name_tag):
            if e.get("name")==name and e.get("type")==type: return e.text.replace(" ","")
        print ("Error")

    def getPathAbs(self): return self.pathAbs
    def getPathScenarios(self): return self.pathScenarios
    def getPathScenario(self): return self.pathScenario
    def getPathTmp(self): return self.pathTmp
    def getNumSim(self):  return self.numSim

def __test (run):
    if run:
        url="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"
        c=Config(url)
        print (c.getPathAbs())
        print (c.getPathScenarios())
        print (c.getPathScenario())
        print (c.getNumSim())


__test(False)
