d={
    'kc':10,'gc':13,'dc':24,'vc':15,'mc':26,'rc':37,'hc':28,'pc':22
}
for k,v in d.items():
    if v>25:
        print(k,end=" ")

d['VC']=19
for k,v in d.items():
    print(f"{k}:{v}")

print(d.get('gc'))
#d.get('lc') -> if not present, it'll give an error :. can give default value as well:
print(d.get('lc','Not Found'))


#student.pop("course")       # removes and returns value of "course"
#student.popitem()           # removes last inserted pair (Python 3.7+)
#del student["grade"]        # delete by key
#student.clear()             # empty dictionary

print("gc" in d)
print("lc" in d)


data = {"a": 1, "b": 2, "c": 3}

data.keys()     # dict_keys(['a', 'b', 'c'])
data.values()   # dict_values([1, 2, 3])
data.items()    # dict_items([('a', 1), ('b', 2), ('c', 3)])

"b" in data     # True
"d" not in data # True

data.update({"d": 4, "a": 10})   # merges another dict → {'a': 10, 'b': 2, 'c': 3, 'd': 4}
