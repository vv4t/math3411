from util import *

def entropy(p, r=2):
  return sum([ -p_i * log_r(p_i, r) for p_i in p ])

def shannon_fano(p, r=2):
  return [ ceil(-log_r(p_i, r)) for p_i in p ]
