#FILTER HOLDS (function,iterables) so:

#odd Num:
def odd(n):
    return n%2==1

print(list(filter(odd,[1,2,3,4,5,6,7,8,9])))
print(list(filter(lambda x: x%2==1,[1,2,3,4,5,6,7,8,9])))

words = ["apple", "banana", "avocado", "grapes", "apricot", "mango"]
print(list(filter(lambda w: w.startswith('a'),words)))
print(list(filter(lambda x: x[0]=='a',words)))

words = ["hi", "hello", "python", "go", "filter", "map"]
print(list(filter(lambda x: len(x)>5,words)))

words = ["apple", "banana", "avocado", "grapes", "apricot", "mango","pineapple"]
print(list(filter(lambda x:"e" in x,words)))

words = ["apple", "banana", "avocado", "grapes", "apricot", "mango","pineapple"]
print(list(filter(lambda x:"a" and "e" in x,words)))