# simulation grid
from learnDyNet.learndynet.learning.learning import Learning
from learnDyNet.learndynet.learning.qLearning import QLearning
from learnDyNet.learndynet.mobility.mobility import Mobility
#from learnDyNet.learndynet.setup.agents import Agents
from learnDyNet.learndynet.reward.reward import Reward
from learnDyNet.learndynet.learning.actionSet import ActionSet
from learnDyNet.learndynet.learning.agents import Agents
from learnDyNet.learndynet.setup.config import Config
from learnDyNet.learndynet.setup.controller import Controller
from learnDyNet.learndynet.network.network import Network
from learnDyNet.learndynet.network.networkGrid import NetworkGrid
from learnDyNet.learndynet.mobility.individuals import Individuals
from learnDyNet.learndynet.learning.stateSet import StateSet

pathConfig="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"

# init config
print("start config and controller")
config=Config(pathConfig)
controller=Controller(config)
controller.initSimulation()

# stateSet
print("start states")
stateSet=StateSet(config)
stateSet.initStates()
print ("states =",len(stateSet.getStateSet()),stateSet.getStateSet())

# actionSet
print("start actions")
actionSet=ActionSet(config,stateSet)
print ("actions =",len(actionSet.getActions()),actionSet.getActions())
stateSet.setAllowedActions(actionSet.getActions())
print (stateSet.getAllowedActionSet())

# network
print("start network")
network=Network(config,stateSet)
networkGrid=NetworkGrid(config,network,stateSet)
networkGrid.initNetwork()
network.setGraph(networkGrid.getGraph())

# agents
print ("start agents")
agents=Agents(config,network,stateSet)
agents.initAgents()
print (agents.getAgents())
network.setAgents(agents)

# learning
print("init learning")
learning=Learning(config,network,stateSet,actionSet,agents)

# individuals
print ("init individuals")
individuals=Individuals(config,network)
individuals.initIndividuals()

# mobility
print ("init mobility")
mobility=Mobility(config,network,individuals)
mobility.initMobility()

# reward
print ("init reward")
reward=Reward(config,network,individuals,agents)


step =0
while step < 5:
    print ("------------------------- step", step)

    # select actions

    # create network
    print ("create network")
    network.createNetwork(step)
    network.displayGraphSimInfo(step)

    # mobility
    print ("start mobility")
    mobility.compute(step)

    # reward
    print ("start reward")
    reward.computeReward(step)
    reward.displayRewards()

    # compute learning
    print ("compute learning")
    learning.compute(step)
    step+=1



quit()
network.setGraph(networkGrid.getGraph())

network.initAgents()
network.setWeights()
print ("end network")
quit()

# learning

learning=Learning(config,network,stateSet,actionSet)




quit()
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

step =1
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


