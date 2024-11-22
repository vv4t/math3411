from math3411 import *
from statistics import mean

m = Polynomial([1,1,1,0,1,0,0,0,1], Z(2))
m3 = Polynomial([1,1,1,1,1], Z(2))
print(m / m3)