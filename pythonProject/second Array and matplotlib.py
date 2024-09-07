import numpy as np

my_current_list = list([2, 3, 4, 5, 66, 7])
my_list = np.flip(my_current_list)
print(my_list)

my_max = np.max(my_current_list) # max point or maximum numbers in list
print(my_max)
my_min = np.min(my_current_list) # minimum number list
print(my_min)
matrix1 = np.array([[1, 2, 3,], [4, 5, 6]]) # this is a math-matrix
matrix2 = np.array([[7, 8], [9, 10], [11, 12]])
#Multiply the matrixces
result = np.dot(matrix1, matrix2) # Multiplication operation for math-matrix
print(result)
# Transpose the matrix
matrix3 = np.array([[1, 2, 3], [5, 6, 99]])
transposed_matrix3 = np.transpose(matrix3)
print(transposed_matrix3)














