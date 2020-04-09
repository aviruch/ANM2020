# Implementation of for solving equations 
import math

def function_exercise(xy):
    x, y = xy
    return [2*x**2 + y**2 - 4.32, x**2 - y**2]

def g1( y ): 
    return math.sqrt(2.16 - 0.5 * y * y)


def g2( x ): 
    return math.sqrt(x*x)


# Function to find the root 
def iterativeSub(xy):
    x,y = xy
    h,g = function_exercise(xy)    
    print ("h and g",h,g)
    t = 0
    while ((abs(h) >= 0.005 or abs(g) >= 0.005) and t < 10) :
        t = t+1
        x1 = g1(y)
        y1 = g2(x)
        x = x1
        y = y1
        xy = x,y
        h,g = function_exercise(xy)
        #print ("x,y",xy)
        print ("x = %0.4f,y=%0.4f" %(x,y))
        print ("h = %0.4f and g=%0.4f" %(h,g))
        
      
    print("The value of the roots  are : %0.4f and %0.4f" % (x,y)) 
##################################################  
# Main starts here
##################################################

xy = [1.0,1.0] # Initial values assumed
 
iterativeSub(xy)

  
#### using Scipy Module

print ("Using Scipy Module")
from scipy.optimize import fsolve

x0 = [1, 1]
sol = fsolve(function_exercise, x0, full_output=1)
print('solution exercice fsolve:', sol)
