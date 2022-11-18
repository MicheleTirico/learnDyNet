from learnDyNet.learndynet.config.config import Config
from learnDyNet.learndynet.learning.learning import Learning
import xml.etree.ElementTree as ET


class StateSet (Learning):
        def __init(self,Learning,config):
                super(StateSet,self).__init__(config)
                print ("a")
                self.__config=config
                self.__stateSet=0
                self.initStates()

        def initStates(self):
                self.__tree=ET.parse(self.__config.pathStates)
                self.__states=self.__tree.getroot()
                print ("ciao")
                for state in self.__states:
                        print (state.tag)

        class State():
                def __init__(self):
                        pass


def __test(run):
        if run:
                url="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"
                config=Config(url)
                learning=Learning(config)
                stateSet=StateSet(config)
                print ("a")



__test(True)