#Write a function valuesort to sort values of a dictionary based on the key.
d={"abc":1,"gc":10,"raha":91,"rajaBabu":1,"jamaila":4,"jaya":96}
print(d)


d_sort=sorted(d.items()) #key based sorting:
print(d)

d_sort2=sorted(d.items(),key= lambda x:x[1])
print(d_sort2)
