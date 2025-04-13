import numpy as np

# 1. Vector with values from 10 to 49
vector = np.arange(10, 50)
print("Vector (10 to 49):\n", vector)

# 2. 3x3 matrix with values from 0 to 8
matrix_3x3 = np.arange(9).reshape(3, 3)
print("\n3x3 Matrix (0 to 8):\n", matrix_3x3)

# 3. 3x3 Identity Matrix
identity_matrix = np.eye(3)
print("\n3x3 Identity Matrix:\n", identity_matrix)

# 4. 3x3x3 array with random values
array_3x3x3 = np.random.rand(3, 3, 3)
print("\n3x3x3 Array with random values:\n", array_3x3x3)

# 5. 10x10 array with random values and find min and max
array_10x10 = np.random.rand(10, 10)
print("\nMin value:", array_10x10.min())
print("Max value:", array_10x10.max())

# 6. Random vector of size 30 and mean value
vector_30 = np.random.rand(30)
print("\nMean value of vector:", vector_30.mean())

# 7. Normalize a 5x5 random matrix
matrix_5x5 = np.random.rand(5, 5)
normalized_matrix = (matrix_5x5 - np.mean(matrix_5x5)) / np.std(matrix_5x5)
print("\nNormalized 5x5 matrix:\n", normalized_matrix)

# 8. Multiply 5x3 by 3x2 matrix (real matrix product)
mat1 = np.random.rand(5, 3)
mat2 = np.random.rand(3, 2)
product_5x2 = np.dot(mat1, mat2)
print("\nProduct of 5x3 and 3x2 matrix:\n", product_5x2)

# 9. Dot product of two 3x3 matrices
A = np.random.rand(3, 3)
B = np.random.rand(3, 3)
dot_product = np.dot(A, B)
print("\nDot product of two 3x3 matrices:\n", dot_product)

# 10. Transpose of a 4x4 matrix
matrix_4x4 = np.random.rand(4, 4)
print("\nTranspose of 4x4 matrix:\n", matrix_4x4.T)

# 11. Determinant of a 3x3 matrix
matrix_3x3_det = np.random.rand(3, 3)
det = np.linalg.det(matrix_3x3_det)
print("\nDeterminant of 3x3 matrix:", det)

# 12. Matrix product of A (3x4) and B (4x3)
A_3x4 = np.random.rand(3, 4)
B_4x3 = np.random.rand(4, 3)
AB_product = np.dot(A_3x4, B_4x3)
print("\nProduct of A (3x4) and B (4x3):\n", AB_product)

# 13. Matrix-vector product (3x3 matrix * 3x1 vector)
M = np.random.rand(3, 3)
v = np.random.rand(3, 1)
mv_product = np.dot(M, v)
print("\nMatrix-vector product:\n", mv_product)

# 14. Solve Ax = b where A is 3x3 and b is 3x1
A_sys = np.random.rand(3, 3)
b_sys = np.random.rand(3)
x_solution = np.linalg.solve(A_sys, b_sys)
print("\nSolution of Ax = b:\n", x_solution)

# 15. Row-wise and column-wise sums of a 5x5 matrix
matrix_5x5_sum = np.random.rand(5, 5)
row_sums = matrix_5x5_sum.sum(axis=1)
col_sums = matrix_5x5_sum.sum(axis=0)
print("\nRow-wise sums:\n", row_sums)
print("Column-wise sums:\n", col_sums)
