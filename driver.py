from math3411 import *

H = Matrix([
  [2,0,0,2,0,1,1],
  [0,1,0,0,1,0,1],
  [0,0,2,1,1,1,0]
], field=GF(3))

codeword = linear_encode(H, [1,2,2,1])

print(find_check_and_info_bits(H))
print(codeword)
