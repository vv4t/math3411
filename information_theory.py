from util import *

def entropy(p, r=2):
  """
  computes shannon entropy H(p)
  p - probability array
  r - radix
  """
  return sum([ -p_i * log_r(p_i, r) for p_i in p ])

def shannon_fano(p, r=2):
  """
  p - probabiltiy array
  r - radix
  returns array of lengths given by shannon code
  combine this with standard_code to generate standard shannon code
  """
  return [ ceil(-log_r(p_i, r)) for p_i in p ]
