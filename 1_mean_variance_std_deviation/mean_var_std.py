import numpy as np

def calculate(numbers):
    values = np.array(numbers).reshape(3, 3)
    calculations = {
    'mean': [values.mean(axis = 0).tolist(), values.mean(axis = 1).tolist(), values.mean().tolist],
    'variance': [values.var(axis = 0).tolist(), values.var(axis = 1).tolist(),  values.var().tolist],
    'standard deviation': [values.std(axis = 0).tolist(), values.std(axis = 1).tolist(),  values.std().tolist],
    'max': [values.max(axis = 0).tolist(), values.max(axis = 1).tolist(),  values.max().tolist],
    'min': [values.min(axis = 0).tolist(), values.min(axis = 1).tolist(),  values.min().tolist],
    'sum': [values.std(axis = 0).tolist(), values.std(axis = 1).tolist(),  values.std().tolist]
    }
    return calculations

user_input = input("Ingrese 9 números separados por espacios: ").strip().split()
user_list = [int(i) for i in user_input]
print(calculate(user_list))

#Create a function named calculate() in mean_var_std.py that uses Numpy to output the mean, variance, standard deviation, max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
#The input of the function should be a list containing 9 digits. The function should convert the list into a 3 x 3 Numpy array, and then return a dictionary containing the mean, variance, standard deviation, max, min, and sum along both axes and for the flattened matrix.

