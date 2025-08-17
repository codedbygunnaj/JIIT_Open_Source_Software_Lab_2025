# 1. Adding elements
nums = [1, 2, 3]
nums.append(4)        # [1, 2, 3, 4]
nums.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
nums.insert(1, 10)    # [1, 10, 2, 3, 4, 5, 6]

# 2. Removing elements
nums.remove(10)       # [1, 2, 3, 4, 5, 6]
nums.pop(2)           # removes element at index 2 → 3
nums.clear()          # []

# 3. Searching & counting
fruits = ["apple", "banana", "apple", "cherry"]
fruits.index("banana")   # 1
fruits.count("apple")    # 2

# 4. Sorting & reversing
marks = [50, 20, 70, 40]
marks.sort()         # [20, 40, 50, 70]
marks.reverse()      # [70, 50, 40, 20]
sorted(marks)        # [20, 40, 50, 70] (returns new list)

# 5. Copying
a = [1, 2, 3]
b = a.copy()         # b = [1, 2, 3]
