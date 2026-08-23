import numpy as np

# Part 1: Create a 1D array and a 2D array using numpy
x = [1,2,5,3,6,4,5 ]
y = np.array(x)
z = np.array([[1,2,3],[9,8,7]])
print ("x = ",x)
print ("y = ", y)
print ("what type is x?",type(x))
print ("what type is y?", type(y))

print ("z = ", z)
# z is a 2D array, so it has 2 dimensions

# Part 2: Create an array from a tuple
w = np.array (((1,2,3),(9,8,7)))
print ("w = ", w)

# np.array is an integer array by default, but we can specify the data type using the dtype argument
a = np.array([[1,2,3],[9,8,7]], dtype = float)

print("a.dtype = ", a.dtype)

# Part 3: How to create an array of zeros, ones, and a constant value
zeros_array = np.zeros((3,7))

print ("zeros_array = ", zeros_array)

ones_array = np.ones((3,2))
print ("ones_array = ", ones_array)


# Part 4: How to create sequence of numbers using np.arange and np.linspace

array_arrange = np.arange( 0, 1.1, 0.2) # (start, stop, step)

print ("array_arrange = ", array_arrange)

array_linspace = np.linspace(.1, 0.7, 5) # (start, stop, number of samples)

print ("array_linspace = ", array_linspace)

# Part 5: Shape Manipulation
a = np.linspace(1,6,6) # Create a 1 by 6 array
b = a.reshape(3,2) # Reshape the array into a 3 by 2 array
print ("a = ", a)

print ("b = ", b)

a = np.array([[1,2,3],[9,8,7]])
b = a.ravel()
print ("a = ", a)
print ("b = ", b)

# Ravel flattens the array into a 1D array.


# Part 6 Universal Operations you can basically use sin, cos, exp. sqrt in the array
a = np.array([[1,2,3], [9,8,7]]) # create a 2 by 3 array
b = np.sin(a)
print (b)

# Basic Operations + * / just use a+5 or a/3 - effects the entire array

# Elementwise Array operations Learn how to do the dot product
# Number 1 Rule in Dot Product, the number of columns must equal the the number of rows in order to multiple

a=np.array([[1,2],[9,8]])
b=np.array([[6,5],[2,4]])
c=a*b # Elementwise multiplication
d=np.dot(a,b) # Mathematical multiplication
print("c = ",c)
print("d = ",d)

# Broadcasting
#** Rule 1: ** Array a's shape is (2,2,3) and array b's shape is (3,). According to
#rule 1 of broadcasting a 1 is prepended to the shape of array b until it has the
#same dimensions as array a i.e. (1,1,3).

#** Rule 2: ** Array b is extended along the dimensions which have size 1 by copying
#the array as many time as needed until it is the same size as array a. This makes
#the size of array b to be (2,2,3) and its content to be [[[6,5,3],[6,5,3]],[[6,5,3],[6,5,3]]].

a=np.array([[1],[2],[3]])
print(" Shape of array a : ",np.shape(a))
b=np.array([4,5,6])
print(np.shape(b))
c=a*b # Elementwise multiplication with broadcasting
print("a times b =" ,c)

a=np.array([[1,3,4],[9,8, 5]])
b=np.array([[3,5,7],[4,2,1],[5,2,7]])
c=np.dot(a,b)
print("dot product =", c)

# Creating n by 1 dimensional vector
# Incorrect
a = np.random.randn(5)
print("a: ",a)
print("a shape : ",a.shape)
print("a transpose: ",a.T)
b=np.dot(a, a.T)
c=np.dot(a.T,a)
print("b : ",b)
print("c : ",c)

# Correct
a = np.random.randn(5, 1) # <--- creates a 2D dimensionsal array
print("a: ",a)
print("a shape : ",a.shape)
print("a transpose: ",a.T)
c=np.dot(a.T,a)
print("b : ",b)
print("c : ",c)