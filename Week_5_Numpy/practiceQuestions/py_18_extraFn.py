import numpy as np

np.linspace(0,10,5) 
# means create 5 evenly spaced number from 0 to 10 i.e [0,2.5,5,7.5,10]

np.zeros(3)
# matrux of zeroes

"""

np.sum()
Calculates the sum of all elements in an array. Like mean, min, and max, you can also use it along a specific axis (e.g., sum of each column or row).

    z = np.array([[1, 2, 3], [4, 5, 6]])
    print(z.sum()) # --> 21

    # Sum along columns (axis=0)
    print(z.sum(axis=0)) # --> [5 7 9]

np.std()
Calculates the standard deviation, a measure of how spread out the numbers in a dataset are. It's a fundamental statistical function.
    z = np.array([1, 2, 3, 4, 5])
    print(np.std(z)) # --> 1.414...

np.sqrt()
Calculates the element-wise square root of every number in an array. This is an example of a NumPy "ufunc" (universal function) that applies an operation to the entire array very efficiently.

    z = np.array([4, 9, 16, 25])
    print(np.sqrt(z)) # --> [2. 3. 4. 5.]

"""

"""

Reshaping and Combining Arrays
These are essential for managing and organizing your data.

.T (Transpose)
The transpose operator (.T) flips an array over its diagonal. It swaps the rows and columns, turning a (3, 2) matrix into a (2, 3) matrix

z = np.array([[1, 2, 3], [4, 5, 6]])
print("Original shape:", z.shape) # --> (2, 3)
print(z)
# [[1 2 3]
#  [4 5 6]]

print("\nTransposed shape:", z.T.shape) # --> (3, 2)
print(z.T)
# [[1 4]
#  [2 5]
#  [3 6]]

"""


"""
np.unique()
Finds and returns the unique elements in an array, sorted. This is incredibly useful for understanding what distinct values exist in your data.

z = np.array([1, 2, 5, 2, 3, 1, 4, 5, 5])
print(np.unique(z)) # --> [1 2 3 4 5]
"""

"""
z = np.arange(10) * 10 # --> [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

# Select the elements at index 2, 5, and 8
indices_to_get = [2, 5, 8]
print(z[indices_to_get]) # --> [20 50 80]

# Select elements in a different order
print(z[[8, 1, 1]]) # --> [80 10 10]
"""