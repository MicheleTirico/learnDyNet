import numpy as np
import networkx as nx

G=nx.grid_graph((3,4))
a=""
b=""
qtab=np.zeros(shape=(1,5,4))
matrix =[a,b,qtab]
nx.set_edge_attributes(G,matrix,"a")
print (matrix)