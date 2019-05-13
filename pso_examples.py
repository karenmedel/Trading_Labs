from pyswarm import pso
import matplotlib.pyplot as plt
import numpy as np
# Then we define the objective function to be minimized, which should be defined like myfunction(x, *args, **kwargs).
# In other words, it takes as its first argument an 1-d array-like object, followed by any other (optional) arguments
# and (again, optional) keyword arguments. The function should return a single scalar value that is minimized.
# In this example, the banana function:
def banana(x):
    x1 = x[0]
    x2 = x[1]
    return -20*np.exp(-0.2*(.5*(x1**2+x2**2)**.5))-np.exp(.5*(np.cos(2*np.pi*x1)+np.cos(2*np.pi*x2)))+np.exp(1)+20

# Optimizing with constraints is optional, but we include one here to illustrate how it might be done in the con
# function which has the same call syntax as the objective, but returns an array of values
# (even if it only has a single value in it):

def con(x):
    x1 = x[0]
    x2 = x[1]
    return [0]
# Rather than specify a starting point for the algorithm, we define the limits of the input variables that the
# optimizer is allowed to search within. For the sake of clarity, we have defined them prior to calling the
# optimizer in the objects lb and ub, which stand for lower-bound and upper-bound, respectively:
lb = [50, 100]
ub = [200, 400]
# That is really all that needs to be defined to run pso, so we then call the optimizer:
# Using the kwarg f_ieqcons tells the routine that there’s a single constraint function that returns an array object.
# Once complete, pso returns two objects: 1) the optimal input values and 2) the optimal objective value.
# The full call syntax for pso is highly customizable and is defined as follows:
xopt, fopt = pso(banana, lb, ub, f_ieqcons=con)
print(xopt)

print('Optimum should be around x=[0.5, 0.76] with banana(x)=4.5 and con(x)=0')

#pso(func, lb, ub, ieqcons=[], f_ieqcons=None, args=(), kwargs={},
    #swarmsize=100, omega=0.5, phip=0.5, phig=0.5, maxiter=100, minstep=1e-8,
    #minfunc=1e-8, debug=False)


x = np.linspace(50.0, 700.0, num=500)
#x = np.linspace(0.0, 10.0, num=5)
y = []
for i in range(len(x)-1):
    #y.append((x[i]+1)/(2*(x[i]**2)))
    #y.append(1/(np.pi*(1+x[i]**2)))
    #y.append(75 + (100/x[i])*np.sin(x[i]))
    y.append(-20*np.exp(-0.2*(.5*(x[i]**2+x[i+1]**2)**.5))-np.exp(.5*(np.cos(2*np.pi*x[i])+np.cos(2*np.pi*x[i+1])))+np.exp(1)+20)
plt.plot(x[:-1], y)
plt.show()
x = np.linspace(500.0, 400.0, num=500)
#x = np.linspace(0.0, 10.0, num=5)
y = []
for i in range(len(x)-1):
    y.append((x[i]+1)/(2*(x[i]**2)))
    #y.append(1/(np.pi*(1+x[i]**2)))
    #y.append(75 + (100/x[i])*np.sin(x[i]))
    #y.append(-20*np.exp(-0.2*(.5*(x[i]**2+x[i+1]**2)**.5))-np.exp(.5*(np.cos(2*np.pi*x[i])+np.cos(2*np.pi*x[i+1])))+np.exp(1)+20)
plt.plot(x[:-1], y)
plt.show()
x = np.linspace(50.0, 400.0, num=500)
#x = np.linspace(0.0, 10.0, num=5)
y = []
for i in range(len(x)-1):
    #y.append((x[i]+1)/(2*(x[i]**2)))
    y.append(1/(np.pi*(1+x[i]**2)))
    #y.append(75 + (100/x[i])*np.sin(x[i]))
    #y.append(-20*np.exp(-0.2*(.5*(x[i]**2+x[i+1]**2)**.5))-np.exp(.5*(np.cos(2*np.pi*x[i])+np.cos(2*np.pi*x[i+1])))+np.exp(1)+20)
plt.plot(x[:-1], y)
plt.show()
x = np.linspace(50.0, 400.0, num=500)
#x = np.linspace(0.0, 10.0, num=5)
y = []
for i in range(len(x)-1):
    #y.append((x[i]+1)/(2*(x[i]**2)))
    #y.append(1/(np.pi*(1+x[i]**2)))
    y.append(75 + (100/x[i])*np.sin(x[i]))
    #y.append(-20*np.exp(-0.2*(.5*(x[i]**2+x[i+1]**2)**.5))-np.exp(.5*(np.cos(2*np.pi*x[i])+np.cos(2*np.pi*x[i+1])))+np.exp(1)+20)
plt.plot(x[:-1], y)
plt.show()
