import numpy as np
import scipy as sp
from scipy import linalg


        


a = sp.array([[2,-3,1],[1,-1,-2],[3,1,-1]])
b = sp.array([7, -2, 0])



x = sp.linalg.solve(a, b)

print(x)
