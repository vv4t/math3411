from lib import *

"""
decode/encode a message using multiple huffman codes from a markov thing
"""

eq = ["00","1","01"]

huff_i = [
  ["10","0","11"],
  ["1","00","01"],
  ["00","1","01"]
]

"""
encode
"""

src = [1,2,3,2,1]

encoded = []
ptr = src[0] - 1
encoded.append(eq[ptr])

for s in src[1:]:
  idx = s - 1
  encoded.append(huff_i[ptr][idx])
  ptr = idx

print("".join(encoded))

exit()
"""
decode
"""

src = "11010000"

decoded = []
ptr = instant_decode(src, eq)[0]
decoded.append(ptr)
src = src[len(eq[ptr]):]

while src != "":
  idx = instant_decode(src, huff_i[ptr])[0]
  decoded.append(idx)
  src = src[len(huff_i[ptr][idx]):]
  ptr = idx

print("".join([ "s" + str(s+1) for s in decoded ]))
