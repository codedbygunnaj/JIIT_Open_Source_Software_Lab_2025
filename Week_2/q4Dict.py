# Finding duplicates in a list
n = [1, 2, 3, 2, 4, 5, 1, 6, 1]

d = {}        # dictionary to store counts
dup = []      # list to store duplicates

# Count occurrences
for i in n:
    if i in d:        # if already present, increase count
        d[i] += 1
    else:             # otherwise start count from 1
        d[i] = 1

# Collect duplicates
for k, v in d.items():
    if v > 1:
        dup.append(k)   # use k (the key), not i

print("Duplicates are:", dup)
