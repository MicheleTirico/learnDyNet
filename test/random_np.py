import numpy as np
import random as rd

l1=list(range(10))
l2=list(range(20))

seed1,seed2=1,2
rd1=np.random.RandomState(seed1)
rd2=np.random.RandomState(seed2)

for i in range(5):
    print (rd1.randint(0,len(l1)))
    print (rd2.randint(0,len(l1)))
