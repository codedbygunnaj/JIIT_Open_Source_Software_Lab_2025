import numpy as np
# 15. How to get the dates of yesterday, today and tomorrow?

yesterday = np.datetime64('today', 'D') - np.timedelta64(1,
'D')
today = np.datetime64('today', 'D')
tomorrow = np.datetime64('today', 'D') +
np.timedelta64(1, 'D')

# 16. How to get all the dates corresponding to the month of July 2016?

Z = np.arange('2016-07', '2016-08', dtype='datetime64[D]')
print(Z)