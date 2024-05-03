import numpy as np
import pandas as pd

# 1. Create numpy array to find the sum of all elements in an array.
arr1 = np.array([1, 2, 3, 4, 5])
sum_arr1 = np.sum(arr1)
print("Sum of all elements in arr1:", sum_arr1)

# 2. Create numpy array of (3,3) dimension. Now find the sum of all rows & columns
# individually. Also find the 2nd maximum element in the array.
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
row_sums = np.sum(arr2, axis=1)
col_sums = np.sum(arr2, axis=0)
second_max = np.partition(arr2.flatten(), -2)[-2]
print("Row sums:", row_sums)
print("Column sums:", col_sums)
print("Second maximum element:", second_max)

# 3. Perform Matrix multiplication of any 2 n*n matrices.
matrix1 = np.array([[1, 2],
                    [3, 4]])
matrix2 = np.array([[5, 6],
                    [7, 8]])
result = np.dot(matrix1, matrix2)
print("Matrix multiplication result:")
print(result)

# 4. Write a Pandas program to get the powers of array values element-wise.
data = {'X': [78, 85, 96, 80, 86], 'Y': [84, 94, 89, 83, 86], 'Z': [86, 97, 96, 72, 83]}
df = pd.DataFrame(data)

# Define a function to calculate powers element-wise
def calculate_power(value, exponent):
    return np.power(value, exponent)

# Apply the function to each element of the DataFrame
powers_df = df.apply(calculate_power, exponent=2)
print("Powers of array values element-wise:")
print(powers_df)


# 5. Write a Pandas program to get the first 3 rows of a given DataFrame.
exam_data = {'name': ['Anastasia', 'Dima', 'Katherine', 'James', 'Emily', 'Michael', 'Matthew', 'Laura', 'Kevin', 'Jonas'],
             'score': [12.5, 9, 16.5, np.nan, 9, 20, 14.5, np.nan, 8, 19],
             'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
             'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
df = pd.DataFrame(exam_data, index=labels)
first_three_rows = df.head(3)
print("First three rows of the DataFrame:")
print(first_three_rows)

# 6. Write a Pandas program to find and replace the missing values in a given DataFrame
# which do not have any valuable information.
df.replace(np.nan, 0, inplace=True)
print("DataFrame after replacing missing values:")
print(df)

# 7. Create a program to demonstrate different visual forms using Matplotlib.
import matplotlib.pyplot as plt

# Example: Plotting a simple line graph
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y)
plt.title("Sine Wave")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
