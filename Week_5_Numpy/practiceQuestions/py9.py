import numpy as np
x=np.ones((10,10))
x[1:-1,1:-1]=0
print(x)

""""
x=np.ones((5,5))
x[1:-1,1:-1]=0 #[rows,cols]
print(x)
"""