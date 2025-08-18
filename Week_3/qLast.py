# Write a function flatten_matrix(matrix) that takes a 2D list and returns a flattened 1D list. Example: [[1, 2], [3, 4]] → [1, 2, 3, 4]

def flat(lis):
    final=[]
    for ls in lis:
        for i in ls:
            final.append(i)

#O(n)

def flat(lis):
    final=[]
    for ls in lis:
        final.extend(ls)

#O(N)