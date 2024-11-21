from math3411 import *

m = Polynomial([1,0,1,1], GF(2))

a = Polynomial([1,0], GF(2))
for i in range(8):
  print(i, "->", a ** i % m)

x = [0,1,0,1]

C_I = Polynomial(list(reversed(x)) + [0] * 3, GF(2))
C_R = C_I % m
C_x = C_I + C_R

d = [0,0,1,1,0,1,1]

D_x = Polynomial(list(reversed(d)), GF(2))

print(D_x.evaluate(a) % m)
