import os
import sys


class Controller:

    def __init__ (self,config):
        self.__config=config
        self.__config.logger.log(cl=self,method=sys._getframe(),message="initialize controller")

    def initSimulation(self):
        paths=[self.__config.pathTmp,self.__config.pathOutputs,self.__config.pathOutput]
        self.__initFolder(paths)


    def __initFolder (self,paths):
        for path in paths :
            self.__config.logger.log(cl=self,method=sys._getframe(),message="create folder in: "+path)
            os.system("mkdir "+path)


    def run (self):
        pass
