import numpy as np

qtab=np.random.rand(2,6,3)
print(qtab)
step=1
action=2
tab=qtab[step]
print (tab)

line=tab[action]
m=max(line)
print (line)
print (m)
