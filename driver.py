from math3411 import *

a = Polynomial([1,0], Z(2))
m = Polynomial([1,1,0,0,1], Z(2))

for i in range(15):
  print(i, "=", a ** i % m)

print("-------------------")

print(m.evaluate(a))
