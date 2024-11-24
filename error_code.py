from util import *
from matrix import *

def ISBN(A):
  return sum([ a*b for (a,b) in zip(A, range(1,len(A)+1)) ]) % 11

def find_check_and_info_bits(H):
  """
  H - parity check matrix of Matrix type
  returns where the check bits and info bits are
  """
  H = H.reduced()
  
  # takes reduced form then has leading entry columns as check bits and the rest as info bits
  check_bits = [ H.lead(row) for row in range(H.height()) ]
  info_bits = [ i for i in range(H.width()) if i not in check_bits ]
  
  return check_bits, info_bits

def linear_encode(H, m):
  """
  H - parity check matrix of Matrix type
  m - array of symbols
  """
  H = H.reduced()
  x = [0] * H.width()
  
  check_bits, info_bits = find_check_and_info_bits(H)
  
  for pos, info in zip(info_bits, m):
    x[pos] = H.field(info)
  
  Hx_T = (H * Matrix([x], H.field).transpose()).transpose()
  
  for pos, check in zip(check_bits, Hx_T.m[0]):
    x[pos] = -check
  
  return x

def packing_bound(len_C, n, t, r):
  """
  len_C - |C|
  n - codeword size
  t - how many can correct
  r - radix
  """
  k = 0
  for i in range(t + 1):
    k += C(n, i) * ((r-1)**i)
  
  return k * len_C, r**n
