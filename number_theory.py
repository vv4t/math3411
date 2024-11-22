import builtins
from math import *

def gcd(a, b):
  if b == 0:
    return a
  x, y = b, a % b
  return gcd(x, y)

def egcd(a, b):
  if a == 0:
    return b, 0, 1
  
  r, x1, y1 = egcd(b%a, a)
  
  x = y1 - x1 * (b//a)
  y = x1
  
  return r, x, y

def phi(n):
  return len([ True for a in range(n) if gcd(a, n) == 1 ])

def order(a, m):
  return [ k for k in range(m) if pow_mod(a,k,m) == 1][1:][0]

def pseudo_prime(n, a):
  if gcd(a, n) != 1:
    return False
  if pow_mod(a, n-1, n) != 1:
    return False
  return True

def strong_pseudo_prime(n, a):
  if not pseudo_prime(n, a):
    return False
  
  s = 0
  t = n - 1
  
  while t % 2 == 0:
    s += 1
    t //= 2
  
  print(f"2^{s} * {t} + 1 = {n}")
  
  if pow_mod(a, t, n) == 1:
    return True
  
  for r in range(s):
    if pow_mod(a, 2**r * t, n) == n - 1:
      return True
  
  return False

def fermat_factorise(n):
  base = ceil(sqrt(n))
  for t in range(base, n):
    s = sqrt(t*t - n)
    if floor(s) == s:
      return tuple(sorted([t+s, t-s]))
  raise 0

def pow_mod(a, b, n):
  return builtins.pow(a, b, n)
