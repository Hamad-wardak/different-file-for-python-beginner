''' Array loop with numpy has many possibilities for solving and calculating in a list especially for integer list'''
import numpy as np

my_array = np.array([2, 3, 4, 55, 690, 77, 88, 90, 909])
my_second_array = np.array([59, 40, 59, 6, 71, 92, 12, 90, 80])
result = my_array + my_second_array # plural tow list in index type
print(result)
my_array = np.median(my_array) #The median number in my_array list
print(my_array)
mean_value = np.mean(my_second_array) # mean  number in this list
print(mean_value)
print('Wow')
mean_value1 = np.median(my_second_array) # Median  or first number in this list
print(mean_value1)

my_second_array = np.sort(my_second_array) # sort the all numbers in this list
print(my_second_array)

