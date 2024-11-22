from util import *

def kraft_mcmillan(l, r):
  """
  l - length array e.g. [1,1,2,3]
  r - radix
  """
  return sum([1.0 / pow(r, l_i) for l_i in l])

def num_to_code(n, r):
  """
  converts "magnitude" into digits array of radix r
  n - magnitude
  r - radix
  e.g. num_to_code(5, 2) -> [1,0,1]
  """
  if n == 0:
    return [0]
  return [ (n // r**i) % r for i in range(floor(log_r(n, r)+1)) ]

def padded_num_to_code(n, r, N):
  c = num_to_code(n, r)
  return c + [0] * (N - len(c))

def standard_code(l, r=2):
  """
  generates standard codes array
  l - length array e.g. [1,1,2,3]
  r - radix
  e.g. standard_code([1,1,2,3]) -> [0,1,00,010]
  """
  
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

def symbol_encode(m, s):
  """
  encodes a message with a set of codewords
  *** STARTS AT INDEX 1
  m - message as array of ints e.g. [1,2,3]
  s - symbol array e.g. ["00", "01", "11"]
  returns e.g. "000111"
  """
  return "".join(s[x - 1] for x in m)

def instant_decode(m, C):
  """
  converts an encoded message into array of symbol indexes given a code set
  m - message str e.g. 010100
  C - codeword set e.g. [1,01,00]
  e.g. instant_decode("010100", [1,01,00]) -> [1,1,2] which is s2s2s3
  """
  s = []
  
  while m:
    for i, c in enumerate(C):
      if m.startswith(c):
        s.append(i)
        m = m[len(c):]
  
  return s

def comma_code(n):
  """
  generate a comma code of length n
  """
  c = []
  for i in range(1,n+2):
    if i == n + 1:
      c.append((i - 1) * "1")
    else:
      c.append((i - 1) * "1" + "0")
  return c
    
    
def huff(p, radix=2, silent=False):
  """
  generates a huffman c
  """
  
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
  
  for x, y, z in zip([-1] + placed_at, phase + [sum(p)], E + [[-1]]):
    info = [
      ((f"[{b}]" if a == x else str(b) + "  ") + ("->" + str(c) if c >= 0 else "")).ljust(12)
      for a, b, c  in zip(range(len(y)), y, z)
    ]
    if not silent: print("".join(info))
  
  C = [ "".join(map(str,c)) for c in C ]
  
  if not silent: 
    print("L =", sum([ a*len(b) for a,b in zip(p, C) ]))
    print("C =", C)
  
  return C
  
def lz78_decode(m):
  """
  returns dictionary and decoded message
  """
  m = [ (int(c[0]), c[1]) for c in m.split(",") ]
  d = [""]
  
  for c in m:
    a, b = c
    d.append(d[a] + b)
  
  return d, "".join(d)

def lz78_encode(m):
  """
  returns dictionary and tuple array
  """
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
  """
  T - interval range e.g. [0.1, 0.2, 0.3, 1.0], where s1 -> [0.1,0.2), s2 -> [0.2, 0.3) etc. ends at 1
  m - message to decode
  """
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
  """
  P - probability array - [ 0.1, 0.1, 0.8 ] so P(s1) = 0.1, P(s2) = 0.2, P(s3) = 0.8
  d - alphabet mapping for message so d='ab*' means m="bba*" becomes s2s2s1s3
  """
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
