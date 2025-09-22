s=input("Enter a string: ")
# n=int(input("Enter a number: "))
lst=s.split(' ')
temp=[]
for i in lst:
    temp.append(i[::-1])
print(' '.join(temp))