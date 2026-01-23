import numpy as np

# 1️⃣ Create a 1D array
arr = np.array([1, 2, 3, 4, 5])
print("Original array:", arr)

# 2️⃣ Basic math operations
print("Array + 10:", arr + 10)
print("Array squared:", arr ** 2)
print("Square root:", np.sqrt(arr))

# 3️⃣ Statistics
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Standard deviation:", np.std(arr))

# 4️⃣ Indexing and slicing
print("First element:", arr[0])
print("Last element:", arr[-1])
print("Elements from index 1 to 3:", arr[1:4])

# 5️⃣ Create a 2D array and do matrix multiplication
mat1 = np.array([[1, 2], [3, 4]])
mat2 = np.array([[5, 6], [7, 8]])
result = mat1 @ mat2   # or np.dot(mat1, mat2)
print("Matrix multiplication result:\n", result)
