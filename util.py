from math import *
from fractions import Fraction

def fact(n):
  return prod(range(1,n+1))

def C(n, k):
  return fact(n) / (fact(n - k) * fact(k))

def log_r(n, r=2):
  return log(n) / log(r)

def log_2(n):
  return log_r(n, 2)

def log_3(n):
  return log_r(n, 3)

def permutate(C):
  P = []
  for i in range(1, len(C) + 1):
    for j in range(len(C) ** i):
      C_i = [ (j // len(C)**k) % len(C) for k in range(i) ]
      s = "".join([ C[k] for k in C_i ])
      P.append(s)
  return P

def has_duplicates(C):
  d = {}
  for c in C:
    if c in d:
      return True
    else:
      d[c] = True
  return False
