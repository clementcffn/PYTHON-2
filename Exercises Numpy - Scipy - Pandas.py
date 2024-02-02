#PYTHON 2

#Exercises: Numpy, Scipy, Pandas
#NUMPY

import numpy as np
import pandas as pd
import scipy as sc

ex1 = np.arange(0,10,0.5)
print(ex1)

n = 10
ex2= np.random.normal(size=n)
print(ex2)

#exercice 3
means = [0,0]
T = 2
correlation = 0.5
N_sample = 5000
covariance_matrix = [[T,T*correlation],[T*correlation,T]]
X = np.random.multivariate_normal(means, covariance_matrix, N_sample)
print(X)
print(X.shape)

#SCIPY
import matplotlib.pyplot as plt

def f(x):
    return x**3-2

x = range(-5,5)
y= [f(xi) for xi in x]
plt.plot(x,y)


from scipy import optimize
root = optimize.newton(f, 2)
print(root)

#################
maturity=[0,1,2,3,4]
observed_default_probabilities=[0.0,0.30, 0.46, 0.58, 0.64]
plt.plot(maturity,observed_default_probabilities)

fitted_coefficient = np.polyfit(maturity, observed_default_probabilities, 2)
fitted_function = np.poly1d(fitted_coefficient)
fitted_coefficient
fitted_function

array_maturity = np.array(maturity)
plt.plot(maturity, fitted_function(maturity), "-", maturity, observed_default_probabilities, "*")


from scipy.optimize import curve_fit
import math

maturity=[0,1,2,3,4]
observed_default_probabilities=[0.0,0.30, 0.46, 0.58, 0.64]

def f_expo(x, lambda_fitted):
    z = 1 - np.exp(-lambda_fitted * x)
    return z

result_lambda = curve_fit(f_expo, maturity, observed_default_probabilities)
result_lambda[0][0]


