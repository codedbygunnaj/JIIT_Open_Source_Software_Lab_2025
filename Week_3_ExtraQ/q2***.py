# Step 2: key parameter

# The real power is in the key function.
# sorted(lst, key=some_function)

# 👉 Each element of list is passed through some_function, and sorting is done based on that function’s output.

words = ["apple", "dog", "banana","cat"]
print(sorted(words, key=lambda x:(len(x),x)))

# means pehle we'll consider lenfth and adter that we'll consider ascii order

files = ["data.txt", "main.py", "readme.md", "index.html"]
print(sorted(files,key= lambda x:(len(x),x)))
print(sorted(files,key= lambda x:(x.split('.')[-1],x)))
# files (html<md<py<txt) ke according sorting
print(sorted(files,key= lambda x:(x.split('.')[-1],x)))

print(sorted(files,key= lambda x:(x.split('.')[-1],x),reverse=True))