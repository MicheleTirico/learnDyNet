# simulation grid
import networkx as nx

from learnDyNet.learndynet.config.config import Config
from learnDyNet.learndynet.controller.controller import Controller
from learnDyNet.learndynet.network.network import Network
from learnDyNet.learndynet.network.networkGrid import NetworkGrid

pathConfig="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"

config=Config(pathConfig)

controller=Controller(config)
controller.initSimulation()

# network
network=Network(config)
networkGrid=NetworkGrid(config,network)
networkGrid.initNetwork()
G=network.getGraph()

network.dispayGraph()


