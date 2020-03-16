# Bisection Method
# The function is x^3 - x -  1 

def func(x): 
    return x * x * x - x - 1

# Function to find the root 
def bisectionMethod(x1,x2):
    k = x2 - x1
       
    while abs(k) >= tolerance:             
        mid = (x1+ x2)/2
        print("mid",mid)
        h = func(mid)
        print("h= %0.5f" %h)              
        
        if h> 0:
            x2 = mid
            
        else: 
            x1 = mid

        k = x2 - x1
        print ("Diff x2 - x1= %0.5f" %k)
    print("The value of the root is : ","%.5f"% mid)
    return x1,x2
  
######################################################
#                  Main Starts Here
######################################################
tolerance = 0.002 # Between x1 and x2
x1 = 1.3 # Initial Lower 
x2 = 1.4 #Initial Upper
p,q = bisectionMethod(x1,x2)
print ("\n Root is between %0.5f and %0.5f" %(p,q))
print ("End")
  

