import numpy as np
nb_classes = 6
targets = np.array([0,1,2,3,2,1,0]).reshape(-1)
one_hot_targets = np.eye(nb_classes)[targets]

print(one_hot_targets)