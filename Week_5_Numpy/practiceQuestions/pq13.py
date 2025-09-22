# common between 2 arrays:
import numpy as np
z=np.arange(11)
Z=np.arange(6)
y=np.intersect1d(z,Z)
print(y)