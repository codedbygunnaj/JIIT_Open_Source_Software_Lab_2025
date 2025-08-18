#largest n numbers:
def fun(lis,n):
    return sorted(lis,reverse=True)[:n]

print(fun([2,5,6,7,1,2,9,8,4,5,6,8],5))