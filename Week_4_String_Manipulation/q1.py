s=input("Enter a string: ")
lst=s.split(' ')
ind=0;maxLen=-1
for i in range(len(lst)):
    if len(lst[i])>maxLen:
        maxLen=len(lst[i])
        ind=i

print(lst[ind])