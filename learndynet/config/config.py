import shutil
import xml.etree.ElementTree as ET
import os
import sys
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
        self.pathAbs = self.__getVal("urls","url","absPath")+"/"
        self.pathScenarios=self.pathAbs+self.__getVal("urls","url","scenarios")+"/"
        self.pathScenario=self.pathScenarios+self.__getVal("urls","url","scenario")
        self.pathTmp=self.pathAbs+self.__getVal("urls","url","tmp")
        self.pathOutputs=self.pathAbs+self.__getVal("urls","url","outputs")+"/"
        self.pathOutput=self.pathOutputs+self.__getVal("urls","url","scenario")
        self.patStates=self.pathAbs+self.__getVal("urls","url","states")

        # parameters simulation
        self.numSim=self.__getVal("simulation","parameter","numsim")

        # parameters
        self.typeNetwork=self.__getValType("network","parameter","typenetwork","val")
        # grid
        self.graph_grid_dimension_x= int(self.__getValType("network","parameter","dimension_x","grid"))
        self.graph_grid_dimension_y= int(self.__getValType("network","parameter","dimension_y","grid"))
        self.graph_grid_dist_x=float(self.__getValType("network","parameter","dist_x","grid"))
        self.graph_grid_dist_y=float(self.__getValType("network","parameter","dist_y","grid"))



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
