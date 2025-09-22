import numpy as np
z=np.arange(11)
# negate between 3 to 8
z[(3<=z)and(z<=8)]*=-1
print(z)


"""

import numpy as np
z=np.arange(11)
# negate between 3 to 8
z[(2>z)|(z>=9)]*=-1
print(z)

[  0  -1   2   3   4   5   6   7   8  -9 -10]

"""