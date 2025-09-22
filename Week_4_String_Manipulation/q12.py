def flatten_matrix(matrix):
  """
  Flattens a 2D list into a 1D list using a for loop.

  Args:
    matrix: A list of lists (2D list).

  Returns:
    A single list containing all elements from the matrix.
  """
  flattened_list = []
  for row in matrix:
    flattened_list.extend(row)
  return flattened_list

# --- Example ---
my_matrix = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
flat_list = flatten_matrix(my_matrix)
print(f"Original Matrix: {my_matrix}")
print(f"Flattened List: {flat_list}")
# Expected Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]