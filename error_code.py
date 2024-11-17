from util import *

def ISBN(A):
  return sum([ a*b for (a,b) in zip(A, range(1,len(A)+1)) ]) % 11
