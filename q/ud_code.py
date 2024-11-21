from lib import *

"""
which from the choices makes the codewords uniquely decodable
"""

codewords = [ "1", "10", "01" ]
choices = [ "00", "0", "11", "000" ]

for c in choices:
  print(c, not has_duplicates(permutate(codewords + [c])))
