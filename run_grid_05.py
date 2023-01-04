# simulation grid
from learnDyNet.learndynet.analysis.plotRewardPerAgent import PlotRewardPerAgent
from learnDyNet.learndynet.learning.learning import Learning
from learnDyNet.learndynet.mobility.mobility import Mobility
from learnDyNet.learndynet.reward.reward import Reward
from learnDyNet.learndynet.learning.actionSet import ActionSet
from learnDyNet.learndynet.learning.agents import Agents
from learnDyNet.learndynet.setup.config import Config
from learnDyNet.learndynet.setup.controller import Controller
from learnDyNet.learndynet.network.network import Network
from learnDyNet.learndynet.network.networkGrid import NetworkGrid
from learnDyNet.learndynet.mobility.individuals import Individuals
from learnDyNet.learndynet.learning.stateSet import StateSet
from learnDyNet.learndynet.storeOutputs.storeAgents import StoreAgents

pathConfig="/media/mtirico/DATA/project/learnDyNet/learnDyNet/scenarios/grid_01/config.xml"

# init config
print("start config and controller")
config=Config(pathConfig)

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
#print (stateSet.getAllowedActionSet())

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
network.setAgents(agents)

# learning
print("init learning")
learning=Learning(config,network,stateSet,actionSet,agents)

# individuals
print ("init individuals")
individuals=Individuals(config,network)
individuals.initIndividuals()
agents.setIndividuals(individuals)


for id, ind in individuals.getIndividuals().items():
    print (id, ind.getTheta())

# mobility
print ("init mobility")
mobility=Mobility(config,network,individuals)
mobility.initMobility()
agents.setMobility(mobility)

# reward
print ("init reward")
reward=Reward(config,network,individuals,agents)

print ("create network")
network.createNetwork(0)
network.displayGraphSimInfo(0)

controller=Controller(config,learning,network,mobility,reward)
controller.initSimulation()

# run
controller.run()
print ("--------------------------------------------------------- finish")
print (agents.getAgents())
for id in agents.getAgents():
    agent=agents.getAgents()[id]
    print ("agent",id)


    print (len(agent.getListStateNotTested()),len(stateSet.getStateSet()))

    for i in list(agent.getQtabList()[config.numStep-1]):        print (list(i))

    print ("rewards of agent",id,":",agent.get_reward())

# store outputs
storeAgents=StoreAgents(config,agents)
storeAgents.compute()

# plot immages
plotRewardPerAgent=PlotRewardPerAgent(config,agents)
plotRewardPerAgent.getPlot()
