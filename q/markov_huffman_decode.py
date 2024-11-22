from lib import *

"""
decode a message using multiple huffman codes from a markov thing
"""

eq = ["01","00","1"]

huff_i = [
  ["00","1","01"],
  ["0","10","11"],
  ["0","10","11"]
]

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
