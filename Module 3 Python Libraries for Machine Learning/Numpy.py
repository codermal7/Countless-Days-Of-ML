# -*- coding: utf-8 -*-
"""Complete Numpy Tutorial in Python

NumPy - Numerical Python

Advantages of Numpy Arrays:

1. Allows several Mathematical Operations
2. Faster operations

"""

from time import process_time
import numpy as np

"""List vs Numpy - Time Taken"""


"""Time taken by a list"""

python_list = [i for i in range(10000)]

start_time = process_time()

python_list = [i+5 for i in python_list]

end_time = process_time()

print(end_time - start_time)

np_array = np.array([i for i in range(10000)])

start_time = process_time()

np_array += 5

end_time = process_time()

print(end_time - start_time)

"""Numpy Arrays"""

# list
list1 = [1, 2, 3, 4, 5]
print(list1)
type(list1)

np_array = np.array([1, 2, 3, 4, 5])
print(np_array)
type(np_array)

# creating a 1 dim array
a = np.array([1, 2, 3, 4])
print(a)

a.shape

b = np.array([(1, 2, 3, 4), (5, 6, 7, 8)])
print(b)

b.shape

c = np.array([(1, 2, 3, 4), (5, 6, 7, 8)], dtype=float)
print(c)

"""Initial Placeholders in numpy arrays"""

# create a numpy array of Zeros
x = np.zeros((4, 5))
print(x)

# create a numpy array of ones
y = np.ones((3, 3))
print(y)

# array of a particular value
z = np.full((5, 4), 5)
print(z)

# create an identity matrix
a = np.eye(5)
print(a)

# create a numpy array with random values
b = np.random.random((3, 4))
print(b)

# random integer values array within a specific range
c = np.random.randint(10, 100, (3, 5))
print(c)

# array of evenly spaced values --> specifying the number of values required
d = np.linspace(10, 30, 5)
print(d)

# array of evenly spaced values --> specifying the step
e = np.arange(10, 30, 5)
print(e)

# convert a list to a numpy array
list2 = [10, 20, 20, 20, 50]

np_array = np.asarray(list2)
print(np_array)
type(np_array)

"""Analysing a numpy array"""

c = np.random.randint(10, 90, (5, 5))
print(c)

# array dimension
print(c.shape)

# number of dimensions
print(c.ndim)

# number of elements in an array
print(c.size)

# checking the data type of the values in the array
print(c.dtype)

"""Mathematical operations on a np array"""

list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

print(list1 + list2)    # concatenate or joins two list

a = np.random.randint(0, 10, (3, 3))
b = np.random.randint(10, 20, (3, 3))

print(a)
print(b)

print(a+b)
print(a-b)
print(a*b)
print(a/b)

a = np.random.randint(0, 10, (3, 3))
b = np.random.randint(10, 20, (3, 3))

print(a)
print(b)

print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.divide(a, b))

"""Array Manipulation"""

array = np.random.randint(0, 10, (2, 3))
print(array)
print(array.shape)

# transpose
trans = np.transpose(array)
print(trans)
print(trans.shape)

array = np.random.randint(0, 10, (2, 3))
print(array)
print(array.shape)

trans2 = array.T
print(trans2)
print(trans2.shape)

# reshaping a array
a = np.random.randint(0, 10, (2, 3))
print(a)
print(a.shape)

b = a.reshape(3, 2)
print(b)
print(b.shape)
