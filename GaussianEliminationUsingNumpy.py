#a = [[1.0,1.0,2.0,-4],[2.0,-1.0,3.0,1],[3.0,1.0,-1.0,2],[1,-1,-1,1]]
#b = [0.0,5.0,5.0,0]

import numpy as np
def gaussElimin(a,b):
    n = len(b)
    # Elimination Phase
    for k in range(0,n-1):
        for i in range(k+1,n):
            if a[i,k] != 0.0:
                lam = a [i,k]/a[k,k]
                #a[i,k+1:n] = a[i,k+1:n] - lam*a[k,k+1:n]
                a[i,:] = a[i,:] - lam*a[k,:]
                b[i] = b[i] - lam*b[k]
    # Back substitution
    for i in range(n-1,-1,-1):
        # range(2,-1,-1) will give 2,1,0
        print ("i=",i)
        x = b[i]
        if i < n-1:
            for j in range(i+1,n):
                print ("j=",j)
                x = x - a[i,j]*b[j]
        b[i] = x / a[i,i]
    return b

# Main starts here 
a = np.array([[2.0,-3.0,1.0],[1.0,-1.0,-2.0],[3.0,1.0,-1.0]])
b = np.array([7.0,-2.0,0.0])

print ("a",a)
print ("b",b)
c = gaussElimin(a,b)
print ("Solution Vector-",c)
