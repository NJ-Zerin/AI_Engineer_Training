import numpy as np

# Create a 1D NumPy array
one_d_array = np.array([10, 20, 30, 40, 50])

# Create a 2D NumPy array
two_d_array = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

# Print arrays
print("1D Array:", one_d_array)
print("2D Array:\n", two_d_array)

# Print shape and data type
print("\n--- Shape and Data Type ---")
print("1D Array Shape:", one_d_array.shape)
print("1D Array Data Type:", one_d_array.dtype)

print("2D Array Shape:", two_d_array.shape)
print("2D Array Data Type:", two_d_array.dtype)

# Perform operations
print("\n--- Operations on 1D Array ---")
print("Sum:", np.sum(one_d_array))
print("Mean:", np.mean(one_d_array))
print("Max:", np.max(one_d_array))
print("Min:", np.min(one_d_array))

print("\n--- Operations on 2D Array ---")
print("Sum:", np.sum(two_d_array))
print("Mean:", np.mean(two_d_array))
print("Max:", np.max(two_d_array))
print("Min:", np.min(two_d_array))

# Slicing arrays
print("\n--- Array Slicing ---")
print("1D Array Slice (index 1 to 3):", one_d_array[1:4])
print("First Row of 2D Array:", two_d_array[0])
print("Top-left 2x2 of 2D Array:\n", two_d_array[0:2, 0:2])
