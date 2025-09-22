s=input("Enter a string: ")
# n=int(input("Enter a number: "))
# lst=s.split(' ')
ctr=1;lst=[]
for i in range(1,len(s)):
    if s[i]==s[i-1]:
        ctr=ctr+1
    else:
        lst.append(s[i-1]+str(ctr))
        ctr=1
# misses the last one as no counter case to go for else loop so add additional:
lst.append(s[len(s)-1]+str(ctr))
print(''.join(lst))