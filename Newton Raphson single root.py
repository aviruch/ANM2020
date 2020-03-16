# Implementation of Newton 
# Raphson Method for solving equations 
  
# An example function whose solution  
# Single root.  


def func( x ): 
    return x*x*x*x - 8*x*x*x + 23*x*x + 16*x - 50
  
# Derivative of the above function  
 
def derivFunc( x ): 
    return 4 * x * x * x - 24 * x* x +46* x +16

  
# Function to find the root 
def newtonRaphson( x ): 
    h = func(x) / derivFunc(x) 
    while abs(h) >= 0.005: 
        h = func(x)/derivFunc(x)
        print ("h",h)
        x = x - h 
      
    print("The value of the root is : ","%.4f"% x) 
  
# Driver program to test above 
x0 = 1 # Initial values assumed 
newtonRaphson(x0) 
  
#### using Scipy Module

from scipy import optimize
root = optimize.newton(func, x0, derivFunc )
print("\n Using Scipy the value of the root is : %0.4f" %root)
