# simulation grid
from learnDyNet.learndynet.learning.learning import Learning
from learnDyNet.learndynet.mobility.mobility import Mobility
from learnDyNet.learndynet.reward.reward import Reward
from learnDyNet.learndynet.setup.actionSet import ActionSet
from learnDyNet.learndynet.setup.agents import Agents
from learnDyNet.learndynet.setup.config import Config
from learnDyNet.learndynet.setup.controller import Controller
from learnDyNet.learndynet.network.network import Network
from learnDyNet.learndynet.network.networkGrid import NetworkGrid
from learnDyNet.learndynet.setup.individuals import Individuals
from learnDyNet.learndynet.setup.stateSet import StateSet

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

# mobility
print ("init mobility")
mobility=Mobility(config,network,individuals)
mobility.initMobility()

# reward
print ("init reward")
reward=Reward(config,network,individuals,agents)

print ("create network")
network.createNetwork(0)
network.displayGraphSimInfo(0)

print ("\n------------------------ start simulation ------------------------------------\n")
step =1
while step < config.numStep:
    print ("------------------------- step", step,"---------------------------------------------")
    #network.displayGraphSimInfo(step-1)

    # select actions
    learning.selectActions(step)

    # create network
    print ("create network")
    network.createNetwork(step)
 #   network.displayGraphSimInfo(step)

    # mobility
    print ("compute mobility")
    mobility.compute(step)

    # reward
    print ("compute reward")
    reward.computeReward(step)
 #   reward.displayRewards()

    # compute learning
    print ("compute learning")
    learning.computeLearning(step)
#    print ("states =",len(stateSet.getStateSet()),stateSet.getStateSet())

    step+=1

print ("--------------------------------------------------------- finish")
for id in agents.getAgents():
    agent=agents.getAgents()[id]
    print ("agent",id)

    s=0
    for state in agent.getStates():
#        print ("step ",s,state,        stateSet.getStatePos(state))
        s+=1

    print (len(agent.getListStateNotTested()),len(stateSet.getStateSet()))

    for s in range(config.numStep-1):
        print("step:",s)
        for i in list(agent.getQtabList()[s]):
            print (list(i))
