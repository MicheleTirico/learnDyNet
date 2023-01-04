import copy

from matplotlib import pyplot as plt

import numpy as np

def computeGreedy(vals):
    vals_average=[]
    vals_update=copy.copy(vals)
    for step in range(nSim):
        epsilon=1-step/nSim
        test=False
        newVal=100#rd_newVal.randint(90,100)
        while test==False:
            if rd_epsilon.rand() < epsilon:
                action_pos=rd_selectAction.randint(0,len(vals_update))
                vals_update[action_pos]=newVal
                test=True
            else:
                maxVal=min(vals_update)
                action_pos=vals_update.index(maxVal)
                vals_update[action_pos]=newVal
                test=True
        vals_average.append(sum(vals_update)/len(vals_update))
    return vals_update,vals_average


def computeRandom(vals):
    vals_average=[]
    vals_update=copy.copy(vals)
    for step in range(nSim):
        newVal=100#rd_newVal.randint(90,100)
        action_pos=rd_selectAction.randint(0,len(vals_update))
        vals_update[action_pos]=newVal
        vals_average.append(sum(vals_update)/len(vals_update))
    return vals_update,vals_average


rd_vals=np.random.RandomState(0)
rd_selectAction=np.random.RandomState(1)
rd_epsilon=np.random.RandomState(2)
rd_newVal=np.random.RandomState(3)
vals=[rd_vals.randint(0,50) for _ in range(100)]
print ("vals",vals)

nSim=600




vals_update_random,vals_random_av=computeRandom(vals)

vals_update_greedy,vals_greedy=computeGreedy(vals)

print ("vals",vals_update_random)
print ("vals",vals_update_greedy)
plt.plot([_ for _ in range(nSim)],vals_random_av,label='random')
plt.plot([_ for _ in range(nSim)],vals_greedy,label="greedy")
plt.legend()
plt.show()