# simulation grid
from learnDyNet.learndynet.setup.agents import Agents
from learnDyNet.learndynet.setup.config import Config
from learnDyNet.learndynet.setup.controller import Controller
from learnDyNet.learndynet.network.network import Network
from learnDyNet.learndynet.network.networkGrid import NetworkGrid
from learnDyNet.learndynet.setup.stateSet import StateSet

pathConfig="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"

config=Config(pathConfig)

controller=Controller(config)
controller.initSimulation()

# network
network=Network(config)
networkGrid=NetworkGrid(config,network)
networkGrid.initNetwork()
G_states=network.getGraph_states()
network.setGraph_states(G_states)
network.init_G_sim()

#stateSet
stateSet=StateSet(config)
stateSet.initStates()
network.setStateSet(stateSet)

# Agents
agents=Agents(config,network,stateSet)
agents.initAgents()

network.update_G_sim()




network.dispayGraph_states(False)
network.dispayGraph_sim(True)


