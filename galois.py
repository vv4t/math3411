from number_theory import egcd

def is_int(b):
  try:
    int(b)
    return True
  except:
    return False

class GF_P:
  def __init__(self, P, N):
    self.P = int(P)
    self.N = int(N)
    self.normalize()
  
  def normalize(self):
    self.N = self.N % self.P
  
  def copy(self):
    return GF_P(self.P, self.N)
  
  def inverse(self):
    r, x, y = egcd(self.N, self.P)
    return GF_P(self.P, x)
  
  def __mod__(a, b):
    return GF_P(self.P, a.N % int(b)) if is_int(b) else NotImplemented
  
  def __neg__(self):
    return GF_P(self.P, -self.N)
  
  def __radd__(b, a):
    return b + a if is_int(a) else NotImplemented
  
  def __rmul__(b, a):
    return b * a if is_int(a) else NotImplemented
  
  def __add__(a, b):
    return GF_P(a.P, int(a) + int(b)) if is_int(b) else NotImplemented
  
  def __sub__(a, b):
    return GF_P(a.P, int(a) - int(b)) if is_int(b) else NotImplemented
  
  def __mul__(a, b):
    return GF_P(a.P, int(a) * int(b)) if is_int(b) else NotImplemented
  
  def __eq__(a, b):
    return (int(a) - int(b)) % a.P == 0 if is_int(b) else NotImplemented
  
  def __truediv__(a, b):
    return a * GF_P(a.P, int(b)).inverse() if is_int(b) else NotImplemented
  
  def __int__(self):
    return self.N
  
  def __repr__(self):
    return str(self.N)

def GF(P):
  return lambda n : GF_P(P, n)
