from util import *

def kraft_mcmillan(r, l):
  return sum([1.0 / pow(r, l_i) for l_i in l])

def num_to_code(n, r):
  if n == 0:
    return [0]
  return [ (n // r**i) % r for i in range(floor(log_r(n, r)+1)) ]

def padded_num_to_code(n, r, N):
  c = num_to_code(n, r)
  return c + [0] * (N - len(c))

def standard_code(l, r=2):
  last = 0
  l_j = 0
  
  c = {}
  
  for l_i in l:
    if l_i != l_j:
      last *= r**(l_i - l_j)
      l_j = l_i
    if l_i not in c:
      c[l_i] = []
    c[l_i].append(num_to_code(last, r))
    last += 1
  
  s = []
  
  for l_i, c_i in c.items():
    for x in c_i:
      s_i = "".join([str(y) for y in [0] * (l_i - len(x)) + x[::-1]])
      s.append(s_i)
  
  return s

def instant_decode(m, C):
  s = []
  
  while m:
    for i, c in enumerate(C):
      if m.startswith(c):
        s.append(i)
        m = m[len(c):]
  
  return s

def comma_code(i, n):
  if i == n + 1:
    return (i - 1) * "1"
  else:
    return (i - 1) * "1" + "0"
