#odd numbers print:

def oddOnly(ls):
    return list(filter((lambda x: x%2==1),ls))

print(oddOnly([1,2,3,4,5,6,7]))


# lambda arguments: expression

f=lambda x:x*5

print(f(5)) 
# anonymous function (function without a name).