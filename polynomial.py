from copy import copy

class Polynomial:
  def __init__(self, coeff, field=int):
    self.field = field
    self.coeff = list(reversed(list(map(field, coeff))))
  
  def copy(self):
    return Polynomial(list(reversed([ copy(x) for x in self.coeff ])), field=self.field)
  
  def shift_left(self, n):
    c = self.copy()
    c.coeff = [0] * n + c.coeff
    return c

  def scalar_multiply(a, n):
    c = a.copy()
    for term in range(len(a.coeff)):
      c.coeff[term] *= n
    return c

  def degree(self):
    for term in range(len(self.coeff)):
      if self[term] != 0:
        return len(self.coeff) - term - 1
    return 0
  
  def lead(self):
    for term in range(len(self.coeff)):
      if self[term] != 0:
        return self[term]
    return self.field(0)
  
  def modulo_divide(n, d):
    q = Polynomial([0], field=n.field)
    r = n
    
    while r.lead() != 0 and r.degree() >= d.degree():
      t = Polynomial([r.lead() / d.lead()], field=n.field).shift_left(r.degree() - d.degree())
      q = q + t
      r = r - d * t
    
    return (q, r)

  def __add__(a, b):
    if len(b.coeff) > len(a.coeff):
      a, b = b, a
    
    c = a.copy()
    
    for term, coeff in enumerate(b.coeff):
      c.coeff[term] += coeff
    
    return c

  def __sub__(a, b):
    return a + b * -1
  
  def __mul__(a, b):
    if type(b) is not Polynomial:
      return a.scalar_multiply(b)
    
    if len(b.coeff) > len(a.coeff):
      a, b = b, a
    
    c = Polynomial([0], field=a.field)
    
    for term, coeff in enumerate(a.coeff):
      c += b.shift_left(term) * coeff
    
    return c
  
  def __eq__(a, b):
    return (a - b).lead() == 0

  def __mod__(a, n):
    q, r = a.modulo_divide(n)
    return r
  
  def __truediv__(a, n):
    q, r = a.modulo_divide(n)
    return q

  def __pow__(a, n):
    a_n = Polynomial([1], field=a.field)
    for i in range(n):
      a_n *= a
    return a_n

  def __getitem__(self, key):
    return self.coeff[-1 - key]

  def __setitem__(self, key, value):
    self.coeff[-1 - key] = value

  def __repr__(self):
    if self.lead() == 0:
      return "0"
    return " + ".join(
      reversed([
        f"{str(coeff) if int(coeff) > 1 else ''}x{'^' + str(term) if term > 1 else ''}"
        if term > 0 else str(coeff)
        for term, coeff in enumerate(self.coeff) if coeff != 0
      ])
    )
