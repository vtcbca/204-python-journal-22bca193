#write anumpy script to create a new shape to an array without changing its data.


import numpy as np 
x=np.array([1,4,3,5,8,2,34,21,37,90,44,32])
y=np.reshape(x,(3,4))
z=np.reshape(y,(4,3))

print("Reshape 3x4 :\n",y)

print("Reshape 3x4 :\n",z)