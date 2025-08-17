#list compression:
n=[i for i in range(0,11)]
print([i for i in n if i%2==0])

#printDuplicates:
n.extend([i for i in range(0,6)])
print(n)

n.sort()
print(n)

#finding duplicates:
d={};dup=[]
for i in n:
    #if i not in dic-> have to start with 1, not like c++:
    if i in d:
        d[i]+=1
    else:
        d[i]=1

for k,v in d.items():
    if v>1:
        dup.append(k)

print(dup)