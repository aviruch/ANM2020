#a = [[1.0,1.0,2.0,-4],[2.0,-1.0,3.0,1],[3.0,1.0,-1.0,2],[1,-1,-1,1]]
#b = [0.0,5.0,5.0,0]

import numpy as np
def BackSubstitution(a,b):
    n = len(b)
    print ("Lenght of matrix is", n)
    c = np.array([0.0,0.0,0.0])
    for i in range(n-1,-1,-1):
        print ("\n")
        # range(2,-1,-1) will give 2,1,0  
        print ("i=",i)
        c[i] = b[i]
##        if i == n-1: # this will make sure for the last row, j loop is not requried.
##            pass
##        else:
##            for j in range(i+1,n): # if i = 1 -> j = 2 , if i = 0 -> j = 1,2
##                print ("j=",j)
##                x = x - a[i,j]*c[j]
##        c[i] = x / a[i,i]
        print ("a",a[i,i+1:n])
        print ("b",c[i+1:n])
        d = np.dot(a[i,i+1:n],c[i+1:n])
        print ("d",d)
        c[i] = (b[i] - d)/a[i,i]
        print ("Vector c",c)
    return c

# Main starts here 
a = np.array([[2.0,-3.0,1.0],[0.0,0.5,-2.5],[0.0,0.0,25.0]])
b = np.array([7.0,-5.5,50.0])

print ("a",a)
print ("b",b)
c = BackSubstitution(a,b)
print ("Solution Vector-",c)
