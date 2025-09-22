import numpy as np
def prime(num):
    cond=int(np.sqrt(num))+1
    for i in range(2,cond):
        if(num%i==0):
            return False
    return True

print(prime(11))
print(prime(400))
print(prime(10))
print(prime(5))
print(prime(3))
print(prime(23))