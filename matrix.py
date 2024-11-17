class Matrix:
  def __init__(self, m, field=int):
    self.field = field
    self.m = [
      list(map(field, row)) for row in m
    ]
  
  def width(self):
    return len(self.m[0])
  
  def height(self):
    return len(self.m)
  
  def copy(self):
    r = []
    
    for row in self.m:
      v = []
      for col in row:
        v.append(col)
      r.append(v)
    
    return Matrix(r, field=self.field)
  
  def row_add(self, a, b, k):
    B = self.copy()
    for i in range(B.width()):
      B.m[a][i] = B.m[a][i] + B.m[b][i] * k
    return B

  def row_set(self, a, k):
    B = self.copy()
    for i in range(B.width()):
      B.m[a][i] = B.m[a][i] * k
    return B
  
  def transpose(self):
    B = self.copy()
    
    for i in range(self.width()):
      for j in range(self.height()):
        B.m[i][j] = self.m[j][i]
    
    return B
  
  def row_echelon_form(self):
    H = self.copy()
    for i in range(self.height()):
      for lead in range(self.width()):
        if H.m[i][lead] == 0:
          continue
        
        if H.m[i][lead] != 1:
          H = H.row_set(i, H.m[i][lead] / H.m[i][lead])
        
        for j in range(self.height() - 1, i, -1):
          if H.m[j][lead] == 0:
            continue
          H = H.row_add(j, i, -H.m[j][lead] / H.m[i][lead])
        break
    return H

  def reduced(self):
    H = self.copy()
    for i in range(1, self.height()):
      for lead in range(self.width()):
        if H.m[i][lead] == 0:
          continue
        for j in range(i - 1, -1, -1):
          if H.m[j][lead] == 0:
            continue
          H = H.row_add(j, i, -H.m[j][lead] / H.m[i][lead])
        break
    return H
  
  def __mul__(A, B):
    if isinstance(B, Matrix):
      C = A.copy()
      for i in range(A.height()):
        for j in range(B.width()):
          S = 0
          for k in range(A.width()):
            S = S + A.m[i][k] * B.m[k][j]
          C.m[i][j] = S
      return C
    else:
      C = A.copy()
      for i in range(A.height()):
        for j in range(A.width()):
          C.m[i][j] = C.m[i][j] * B
      return C
    
  
  def __repr__(self):
    return "\n".join(repr(row) for row in self.m)
