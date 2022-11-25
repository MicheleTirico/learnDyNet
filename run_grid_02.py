# simulation grid
from learnDyNet.learndynet.learning.qLearning import QLearning
from learnDyNet.learndynet.mobility.mobility import Mobility
#from learnDyNet.learndynet.setup.agents import Agents
from learnDyNet.learndynet.reward.reward import Reward
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

#stateSet
stateSet=StateSet(config)
stateSet.initStates()

# network
network=Network(config,stateSet)
networkGrid=NetworkGrid(config,network,stateSet)
networkGrid.initNetwork()
network.setGraph(networkGrid.getGraph())
network.initAgents()
network.setWeights()
print ("end network")

# agents
print ("agents")
agents=Agents(config,network,stateSet)
agents.initAgents()

# individuals
individuals=Individuals(config,network)
individuals.initIndividuals()
print ("end individuals")

mobility=Mobility(config,network,individuals)
mobility.initMobility()
reward=Reward(config,network,individuals,agents)
learning=QLearning(config,network,agents)

step =0
while step < 5:
    print ("------------------------- step", step)
    # mobility

    print ("start mobility")
    mobility.compute()

    # reward
    print ("start reward")
    reward.computeReward(step)

    # compute learning
    print ("compute learning")
    learning.computeLearning(step)
    step+=1





quit()

G=network.getGraph()
for e in G.edges(data=True):
    print (e)


#network.init_G_sim()

#network.setStateSet(stateSet)

# Agents
agents=Agents(config,network,stateSet)
agents.initAgents()

# individuals
individuals=Individuals(config,network)
individuals.initIndividuals()

# mobility
mobility=Mobility(config,network,individuals)
mobility.initMobility()
mobility.compute()

network.setWeights()



#print (individuals.getIndividuals())
#print (individuals.getIndividual(1))
#quit()





network.dispayGraph(False)


