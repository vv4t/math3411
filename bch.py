import os
os.chdir("..")
from math3411 import *


m1 = Polynomial([1,0,0,1,1], Z(2))
m3 = Polynomial([1,1,1,1,1], Z(2))
m = m1 * m3

message = [0,0,0,0,1,0,0]

C_I = Polynomial(list(reversed(message)) + [0] * 8, Z(2))
C_R = C_I % m
C_x = C_I + C_R

print("encoded message", C_x, "".join(map(str, C_x.coeff)))

print("----------------------------")
a = Polynomial([1,0], Z(2))
for i in range(15):
  print(i, "->", a ** i % m1)
print("----------------------------")

d = [1,0,0,1,1,1,0,1,1,0,1,1,1,0,1]

D_x = Polynomial(list(reversed(d)), Z(2))

# here, match syndromes to primitive power

print(D_x.evaluate(a) % m1)
print(D_x.evaluate(a ** 3) % m1)

# then change what the i,j pair should look for

pairs = []

for i in range(15):
  for j in range(i+1, 15):
    if (a**i + a**j) % m1 == (a**13 % m1):
      pairs.append((i, j))

for x,y in pairs:
  if (a**(3*x) + a**(3*y)) % m1 == (a**14 % m1):
    print(x,y)
    break

d[x] = (d[x] + 1) % 2
d[y] = (d[y] + 1) % 2

y = "".join(map(str,d))
print(y[:8], y[8:])

