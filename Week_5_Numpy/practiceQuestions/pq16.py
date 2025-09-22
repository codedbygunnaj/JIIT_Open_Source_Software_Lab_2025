import numpy as np
x=np.random.randint(0,2,7)
y=np.random.randint(0,2,7)

equal=np.allclose(x,y)
print(equal)

equal=np.array_equal(x,y)
print(equal)

