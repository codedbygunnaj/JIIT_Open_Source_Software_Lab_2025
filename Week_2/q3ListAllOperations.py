# ========================
# Dictionary Operations in Python
# ========================

# 1. Creating a dictionary
student = {"name": "Amit", "age": 20, "course": "Python"}

# 2. Accessing values
print(student["name"])             # Access using key → "Amit"
print(student.get("age"))          # Safe access → 20
print(student.get("grade", "NA"))  # Returns "NA" if key not found

# 3. Adding & Updating
student["grade"] = "A"             # Add new key
student["age"] = 21                # Update existing value
print(student)

# 4. Removing elements
student.pop("course")              # Remove key "course"
print(student)

student.popitem()                  # Remove last inserted item
print(student)

del student["grade"]               # Delete using del
print(student)

student.clear()                    # Remove all items → {}
print(student)

# 5. Useful dictionary methods
data = {"a": 1, "b": 2, "c": 3}
print(data.keys())                 # dict_keys(['a', 'b', 'c'])
print(data.values())               # dict_values([1, 2, 3])
print(data.items())                # dict_items([('a', 1), ('b', 2), ('c', 3)])

print("b" in data)                 # True
print("d" not in data)             # True

# 6. Merging dictionaries
data.update({"d": 4, "a": 10})     # Update/merge keys
print(data)                        # {'a': 10, 'b': 2, 'c': 3, 'd': 4}

# 7. Copying dictionary
copy_data = data.copy()
print(copy_data)
