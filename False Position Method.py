# Method of False Position
# The function is x^3 - x -  1 

def func(x): 
    return x * x * x - x - 1

  
# Function to find the root 
def FalsePositionMethod(x1,x2):
    h = func(x2)
    t = 0
    while t < 15 and abs(h) > tolerance :
        t = t+1 
        xnew = x1 -  func(x1)* ((x2 - x1) / (func(x2)- func(x1)))
        print("xnew = %0.5f" %xnew)   
        if func(xnew)* func(x1) < 0:
            x2 = xnew
        else:
            x1 = xnew
            
        h = func(xnew)
        print("h = func(xnew)= %0.5f" %h)           
    print("The value of the root is : ","%.5f"% xnew)
    return xnew
  
#######################################################
#                   Main Starts Here
#######################################################
tolerance = 0.0001
x1 = 1.3 # Initial Lower 
x2 = 1.4 #Initial Upper
p = FalsePositionMethod(x1,x2)
print ("\nThe root of equation is %0.5f " %(p))
print ("End")
  

