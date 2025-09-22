import numpy as np
x=np.ones((5,5))

# adding zero border on this:
x=np.pad(x,pad_width=1,mode='constant',constant_values=4)
print(x)