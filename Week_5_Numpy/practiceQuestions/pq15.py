# First learn and study all practice questions then we'll move to week questions:
import numpy as np
print(np.datetime64('TODAY','D'))
# print(np.timedelta64(1,'D')) => means 1 day :. subtract or add to get yesterday or tomorrow:

print(np.datetime64('TODAY','D')-np.timedelta64('1','D'))
print(np.datetime64('TODAY','D')+np.timedelta64('1','D'))

# whole month:
z=np.arange('2016-04','2016-04-10',dtype='datetime64[D]')
print(z)