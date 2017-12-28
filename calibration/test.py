import numpy as np

modes = np.arange(3)
nodes = np.arange(7)

U = np.empty((len(nodes), 6, len(modes)))
for mode in modes:
    for node in nodes:
#        U[node,:,mode] = np.random.rand(6)
        a = np.arange(6)
        U[node,:,mode] = a
