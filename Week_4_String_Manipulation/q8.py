import numpy as np
s=input("Enter a string: ")
lst=(s.split(' '))
nums=[int(x) for x in lst]
mean=np.mean(nums)
ctr=0
for i in nums:
    if i>mean:
        ctr=ctr+1

print(ctr)

# mean = sum(nums) / len(nums)