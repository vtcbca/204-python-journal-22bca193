#scrpit to create a 3x3 matrix with values ranging from 2 to 10.output

import numpy as np 

a1 = np.arange(2,11).reshape(3,3)
print(f"Your 3x3 matarix:\n{a1}")
print(f"Dimention of array is = {a1.ndim}\nsize of array = {a1.size}\nBytes occupied memory = {a1.size*a1.itemsize}")
