from scipy.interpolate import *
x = [0,2,4]
y = [0,4,16]
p = lagrange(x,y)
print(p)
