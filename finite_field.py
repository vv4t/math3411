from number_theory import egcd

def is_int(b):
  try:
    int(b)
    return True
  except:
    return False

class Z_p:
  def __init__(self, P, N):
    self.P = int(P)
    self.N = int(N)
    self.normalize()
  
  def normalize(self):
    self.N = self.N % self.P
  
  def copy(self):
    return Z_p(self.P, self.N)
  
  def inverse(self):
    r, x, y = egcd(self.N, self.P)
    return Z_p(self.P, x)
  
  def __mod__(a, b):
    return Z_p(self.P, a.N % int(b)) if is_int(b) else NotImplemented
  
  def __neg__(self):
    return Z_p(self.P, -self.N)
  
  def __radd__(b, a):
    return b + a if is_int(a) else NotImplemented
  
  def __rmul__(b, a):
    return b * a if is_int(a) else NotImplemented
  
  def __add__(a, b):
    return Z_p(a.P, int(a) + int(b)) if is_int(b) else NotImplemented
  
  def __sub__(a, b):
    return Z_p(a.P, int(a) - int(b)) if is_int(b) else NotImplemented
  
  def __mul__(a, b):
    return Z_p(a.P, int(a) * int(b)) if is_int(b) else NotImplemented
  
  def __eq__(a, b):
    return (int(a) - int(b)) % a.P == 0 if is_int(b) else NotImplemented
  
  def __truediv__(a, b):
    return a * Z_p(a.P, int(b)).inverse() if is_int(b) else NotImplemented
  
  def __int__(self):
    return self.N
  
  def __repr__(self):
    return str(self.N)

def Z(P):
  return lambda n : Z_p(P, n)
