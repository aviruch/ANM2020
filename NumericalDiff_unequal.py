

def LagrangeDiffAlgo(x,y, index):    
    sum = 0
    for j in range(len(x)):        
        m = 1
        n = 0
        for k in range(len(x)):            
            if j != k:                
                m = m * 1/(x[j]-x[k])
                n = n + (x[index]-x[k])        
        sum = sum + (n*m) * y[j]
        print ("sum",sum)
        
    return sum

# Main starts here

x  = [0,1.25,3.75]
y  = [13.5,12,10]

index = 0

print ("xx",index)
print ("LagrangeDiff at x =0 is {:0.4f}" .format(LagrangeDiffAlgo(x,y, index)))

import numpy as np
print("Using Numpy",np.gradient(y, x))
