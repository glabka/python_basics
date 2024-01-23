import numpy as np
import pandas as pd
import copy
import scipy.stats as stats
import sympy as sym
import sympy.plotting.plot as symplot
import matplotlib.pyplot as plt # for symplot
from IPython.display import display # for latex-like display of sym's expressions

# -------------------- copy --------------------
list = [1, 2, 3]
list2 = copy.deepcopy(list)
list[2] = -5
print(list)
print(list2)

# -------------------- numpy --------------------
list = [1, 2, 3, 4, 5]
list_mean = np.mean(list)
print(list_mean)
ndarrayObject = np.array(list)
print(type(list))
print(type(ndarrayObject)) # ndarray - n dimensional array - numpy's data type

# in-place vs out of place
n1 = np.array([2, 4, 3, 7, 5])
n2 = np.array(n1) # copying n1

print(n1)
n1.sort()
print(n1) # n1 itself is sorted

print(n2)
np.sort(n2) # only returns sorted n2
print(n2) # n2 itself is not sorted

np.random.randn() # random number from gaussian (normal) distribution
np.random.randn(5) # 5 random numbers
np.random.randn(3, 3) # matrix of random numbers

print(f"ndarray= {n1}, ndarray^2 = {n1**2}, log(ndarray) = {np.log(n1)}")

matrix = np.array([[1, 2, 3], [2, 3, 4], [3, 4, 5], [4, 5, 6]])
print(matrix)
print(matrix.shape) # dimensions

matrix_zeros = np.zeros(matrix.shape) # matrix of zeros the same size as original matrix

# column vector
v_c = np.array([[1], [0], [2], [3]]) # column vector
v_c2 = np.array([1, 0, 2, 3], ndmin=2).T # ndmin = n dimensions minimal; T stands for transpose
print(f"column vector: {v_c}")
print(f"column vector: {v_c2}")

# some other useful operations
v = np.arange(9)
M = np.reshape(v, (3, 3))
C = np.tile(M, (3, 1))
B = C * np.reshape(v, (len(v), 1))
print(v)
print(M)
print(C)
print(B)

# Variance
n = [1, 2, 3, 4, 5, 10, 25]
print(f"biased variance = {np.var(n)}")
print(f"unbiased variance = {np.var(n, ddof=1)}") # degrees of freedom -> results in devision by (n - 1) in the formula

# Taking random subset
n = [1, 2, 3, -2, 0, 10, 59, -40]
print(np.random.choice(n, size=5, replace=False)) # replace -> sample can be taken more times

# -------------------- pandas --------------------
# for tables

# ceatin of random nums
var1 = np.random.randn(100) * 5 + 20
var2 = np.random.randn(100) > 0

# variable names
labels = ['Temp (C)', 'Ice Cream']

# put them together into dictionary
D = {labels[0]:var1, labels[1]:var2}

# into panda
df = pd.DataFrame(data=D)
print(df)
print("count")
print(df.count())
print("head")
print(df.head())
print("mean")
print(df.mean())

# -------------------- scipy.stats --------------------
n1 = 30 # samples in dataset 1
n2 = 40 # samples in dataset 2
mu1 = 1 # population mean in dataset 1
mu2 = 1.2 # population mean in dataset 2

# generating data
data1 = mu1 + np.random.randn(n1)
data2 = mu2 + np.random.randn(n2)

t, p = stats.ttest_ind(data1, data2) # ttest independance -> returns t and p values. Tests hypothesis that the two datasets are from the same distribution
print(t) # t value
# p value - we can compare it with our statistical significance threshold. If it's smaller than that, it says something
# along the lines of the probability of the distributions being the same is smaller than threshold -> thus proving that
# they are actually different (for example that one model performs significantly better than the other).
print(p)

# -------------------- sympy (sym), sympy.plotting.plot (symplot) and IPython.display --------------------
# creating symbolic variable
x = sym.symbols('x')

# creating a function
fx = 2 * x**2

# computing derivative
df = sym.diff(fx, x)

print(fx)
print(df)
display(fx) # should work in PyCharm for instance
display(df)

symplot(fx, (x, -4, 4), title='The function')
plt.show()

symplot(df, (x, -4, 4), title='The functions derivative')
plt.show()

lamb = sym.lambdify(x, df) # returns a function that can be used to compute the value of fx for a given x
