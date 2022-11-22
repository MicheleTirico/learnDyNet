# simulation grid
from learnDyNet.learndynet.setup.agents import Agents
from learnDyNet.learndynet.setup.config import Config
from learnDyNet.learndynet.setup.controller import Controller
from learnDyNet.learndynet.network.network import Network
from learnDyNet.learndynet.network.networkGrid import NetworkGrid
from learnDyNet.learndynet.setup.individuals import Individuals
from learnDyNet.learndynet.setup.stateSet import StateSet

pathConfig="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"

config=Config(pathConfig)

controller=Controller(config)
controller.initSimulation()

# network
network=Network(config)
networkGrid=NetworkGrid(config,network)
networkGrid.initNetwork()
network.setGraph(networkGrid.getGraph())
#network.init_G_sim()

#stateSet
stateSet=StateSet(config)
stateSet.initStates()
network.setStateSet(stateSet)

# Agents
agents=Agents(config,network,stateSet)
agents.initAgents()
# individuals
individuals=Individuals(config,network)
individuals.initIndividuals()

print (individuals.getIndividuals())

print (individuals.getIndividual(1))
quit()





network.dispayGraph(False)


