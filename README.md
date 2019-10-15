# numpy

import numpy as np

# Create an array of ones
n = np.ones((3,4))

print("np.ones: ",n)
# Create an array of zeros

n=np.zeros((2,3,4),dtype=np.int16)
print("np.zeros: ",n)

# Create an array with random values
n=np.random.random((2,2))
print("random.random: ",n)

# Create an empty array
n=np.empty((3,2))
print("empty: ",n)

# Create a full array
n=np.full((2,2),7)
print("full: ",n)

# Create an array of evenly-spaced values
n=np.arange(10,25,5)
print("arange: ",n)

# Create an array of evenly-spaced values
n=np.linspace(0,2,9)
print("linspace: ",n)

n = np.eye(5)
print("np.eye: ",n)

n = np.identity(5)
print("np.identity: ",n)

# Import
x, y, z = np.loadtxt('text-file.txt', skiprows=1, unpack=True)

print("loadtxt ")
print("x: ",x)
print("y: ",y)
print("z: ",z)

my_array2 = np.genfromtxt('text-file.txt',
                      skip_header=1,
                      filling_values=-999)

print("my_array2: ",my_array2)

n = np.eye(5)
m=np.full((2,2),7)

np.save('test',n)

nHIGH=np.eye(50)
np.savez('testH',nHIGH)
np.savez_compressed('testH-c',nHIGH)

my_array=np.full((12,12),70)
# Print the number of `my_array`'s dimensions
print(my_array.ndim)

# Print the number of `my_array`'s elements
print(my_array.size)

# Print information about `my_array`'s memory layout
print(my_array.flags)

# Print the length of one array element in bytes
print(my_array.itemsize)

# Print the total consumed bytes by `my_array`'s elements
print(my_array.nbytes)
np.savez('my_array',my_array)

x=np.random.random((3,4))
y=np.random.random((5,1,4))

# Add `x` and `y`
res=np.add(x,y)
print('res: ',res)

res2=res.sum()
print('res2: ',res2)

my_2d_array=np.random.random((4,4))

# Select the element at row 1 column 2
print(my_2d_array[1][2])

# Select the element at row 1 column 2
print(my_2d_array[1,2])
