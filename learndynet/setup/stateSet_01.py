from learnDyNet.learndynet.setup.config import Config
import xml.etree.ElementTree as ET


class StateSet ():
    def __init__(self,config):
        self.__config=config
        self.__stateSet={}
        self.__tree=ET.parse(self.__config.pathStates)
        self.__states_xml=self.__tree.getroot()

    def initStates(self):
        for state_xml in self.__states_xml:
            name=state_xml.attrib["name"]
            state=State(name)
            for line in state_xml:
                if line.tag=="description":
                    description=line.text
                    state.setDescription(description)
                else:
                    modes=line.attrib["modes"]
                    lines=line.attrib["lines"]
                    cost=line.attrib["cost"]
                    dir=line.attrib["dir"]
                    l=[modes,lines,cost,dir]
                    state.setLine(l)
            self.__stateSet[name]=state

    def getListStates(self):    return list(self.__stateSet.keys())
    def getStates(self):        return self.__stateSet
    def getState(self,name):    return self.__stateSet[name]
    def getNstates(self):       return len(self.__stateSet)

class State():
    def __init__(self, name):
        self.__name=name
        self.__lines=[]
        self.__description=""

    def getName(self):                      return self.__name
    def getLines(self):                     return self.__lines
    def getDescription(self):               return self.__description
    def setLine(self,line):                 self.__lines.append(line)
    def setDescription(self,description):   self.__description=description

def __test(run):
    if run:
        url="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"
        c=Config(url)
        ss=StateSet(c)
        ss.initStates()

__test(True)



"""    
    def setModes(self,modes):              self.__modes=modes
    def setLines(self,lines):              self.__lines=lines
    def setDir(self,dir):                  self.__dir=dir
"""
