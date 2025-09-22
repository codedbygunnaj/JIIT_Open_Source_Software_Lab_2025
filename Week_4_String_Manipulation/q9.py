s=input("Enter a string: ")
dic={"lower":0,"upper":0}
for i in s:
    if i.islower():
        dic["lower"]=dic["lower"]+1
    else:
        dic["upper"]=dic["upper"]+1

str=""
for i in s:
    if i.islower():
        str=str+i.upper()
    else:
        str=str+i.lower()

print(dic)
print(str)
# print()
# print(''.join(lst))