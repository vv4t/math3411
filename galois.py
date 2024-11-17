from number_theory import egcd

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
    c = a.copy()
    c.N = a.N % int(b)
    c.normalize()
    return c
  
  def __radd__(B, A):
    return B + A
  
  def __rmul__(B, A):
    return B * A
  
  def __add__(a, b):
    return GF_P(a.P, int(a) + int(b))
  
  def __sub__(a, b):
    return GF_P(a.P, int(a) - int(b))
  
  def __mul__(a, b):
    return GF_P(a.P, int(a) * int(b))
  
  def __eq__(a, b):
    return (int(a) - int(b)) % a.P == 0
  
  def __truediv__(a, b):
    return a * GF_P(a.P, int(b)).inverse()
  
  def __int__(self):
    return self.N
  
  def __repr__(self):
    return str(self.N)

def GF(P):
  return lambda n : GF_P(P, n)
