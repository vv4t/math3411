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
    
def huff(p, radix=2):
  
  pad = 0
  
  if radix > 2:
    while len(p) % (radix - 1) != 1:
      p += [0]
      pad += 1
  p = sorted(p, reverse=True)
  
  # sum lowest symbols and get index of highest symbol its greater than
  x = p.copy()
  y = p[:-radix].copy() # symbols without lowest 'radix' amount
  s = sum(p[-radix:])
  highest = ([ i for i in range(len(y)) if y[i] <= s ] or [len(y)])[0]
  placed_at = []
  
  E = []
  phase = [x]
  
  while len(x) != radix:
    sE = []
    for i in range(highest):
      # map higher symbols to themselves
      sE.append(i)
    for i in range(highest, len(y)):
      # map lower symbols to one lower than before
      sE.append(i + 1)
    for i in range(len(y), len(y) + radix):
      # map the lowest symbols to new merged symbol
      sE.append(highest)
    E.append(sE)
    placed_at.append(highest)
    phase.append(y)
    
    # insert new symbol at highest position
    y.insert(highest, s)
    x = y.copy()
    y = x[:-radix].copy()
    s = sum(x[-radix:])
    
    if len(x) == radix:
      # point the rest of symbols to single symbol
      E.append([0] * radix)
      placed_at.append(0)
      phase.append([s])
    else:
      highest = ([ i for i in range(len(y)) if y[i] <= s ] or [len(y)])[0]
  
  C = []
  
  for i in range(len(p)):
    pos = i
    codeword = []
    for layer in E:
      if pos >= len(layer) - radix:
        codeword.append(pos - (len(layer) - radix))
      pos = layer[pos]
    C.append(list(reversed(codeword)))
  
  for x, y in zip([-1] + placed_at, phase + [sum(p)]):
    print("".join([ (f"[{b}]" if a == x else str(b)).ljust(8) for a,b in enumerate(y) ]))
  
  print("codeword:", C)
  
def lz78_decode(m):
  m = [ (int(c[0]), c[1]) for c in m.split(",") ]
  d = [""]
  
  for c in m:
    a, b = c
    d.append(d[a] + b)
  
  return d, "".join(d)

def lz78_encode(m):
  d = [ "" ]
  l = 0
  c = []
  while len(m) > 0:
    idx = [ i for i in range(len(d) - 1, -1, -1) if m.startswith(d[i]) ][0]
    new = d[idx] + m[len(d[idx])]
    c.append((idx, new))
    d.append(new)
    m = m[len(d[idx])+1:]
  
  return d, c

def arithmetic_decode(T, m):
  s = []
  
  u = 0.0
  v = 1.0
  
  T = [ (T[i], T[i + 1]) for i in range(len(T) - 1)]
  for X in range(4):
    for itvl, idx in zip(T, range(len(T))):
      a, b = itvl
      x = u + a * (v - u)
      y = u + b * (v - u)
      if m >= x and m < y:
        s_i = idx
        u = x
        v = y
        break
    if s_i is None:
      print("error", s, u, v, m)
    s.append(s_i)
    if s_i == len(T) - 1:
      break
  
  print("".join([ "s"+str(s_i+1) for s_i in s if s_i != len(T) - 1]) + "*")

def arithmetic_encode(P, d, m):
  D = {}
  t = 0.0
  for a, b in zip(d, P):
    D[a] = (t, t + b)
    t += b
  s = 0.5
  for c in m[::-1]:
    x, y = D[c]
    s = x + s * (y - x)
  
  print(s)
