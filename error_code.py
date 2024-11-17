from util import *
from matrix import *

def ISBN(A):
  return sum([ a*b for (a,b) in zip(A, range(1,len(A)+1)) ]) % 11

def find_check_and_info_bits(H):
  H = H.reduced()
  
  check_bits = [ H.lead(row) for row in range(H.height()) ]
  info_bits = [ i for i in range(H.width()) if i not in check_bits ]
  
  return check_bits, info_bits

def linear_encode(H, m):
  x = [0] * H.width()
  
  check_bits, info_bits = find_check_and_info_bits(H)
  
  for pos, info in zip(info_bits, m):
    x[pos] = H.field(info)
  
  Hx_T = (H * Matrix([x], H.field).transpose()).transpose()
  
  for pos, check in zip(check_bits, Hx_T.m[0]):
    x[pos] = check
  
  return x
