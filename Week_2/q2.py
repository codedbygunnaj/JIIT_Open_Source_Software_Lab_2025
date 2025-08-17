t=(
    'Ram','Shyam','Gyaan','Ryaan','Ryan','Kian','Lion','Mayan','Vaaroon','Vian'
)
print(t)
#can't edit in tuple, have to make it list:
l=list(t)
#last number insertion
l.append('Jian')
#any number insertion
l.insert(5,'Gian')
t=tuple(l)

print(t)
#can't edit in tuple, have to make it list:
l=list(t)
#any random number deletion
l.pop()
print(l)
#particular index deletion:
l.remove('Gian')
t=tuple(l)
print(t)

print(t[0:4])

l=list(t)
l[2]='Tian'
print(l)
t=tuple(l)
print(t)
