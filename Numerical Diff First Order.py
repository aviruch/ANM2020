import numpy as np
import math

def f(x):
    return -0.1 * x**4 - 0.15 * x**3 - 0.5 * x**2 - 0.25 * x + 1.2
    ##return math.sin(x)
    #return x*x*x - 5

def forwardDifference(f,a,h,x):

	# Write your code here
    
    return dydx_forward_diff

def backwardDifference(f,a,h,x):    
	
	# Write your code here
    
    return dydx_backward_diff


def centralDifference(f,a,h,x):    
	
	# Write your code here
    
    return dydx_cen_diff  

################################
# Main starts here
################################

#x = [0.40,0.60,0.8,1.0,1.2]
x = np.arange(0,1.5,0.50)

print ("x",x)
h = x[1]-x[0]
print ("h=", h)

a = 0.5
# calculate y'(0.5)
dydx = forwardDifference(f,a,h,x)
print ("dydx={:0.4f}" .format(dydx))










    
