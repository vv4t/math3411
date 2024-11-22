
def I_c(freqs, n):
  """
  calculate index of coincidence
  freq - frequencies
  n - length of text
  """
  return (sum([freq**2 for freq in freqs]) - n) / (n**2 - n)

def I_c_from_text(text):
  """
  calculate index of coincidence in some text
  """
  d = {}
  for c in text:
    if c not in d:
      d[c] = 0
    d[c] += 1
  return I_c(list(d.values()), len(text))

def estimate_r(I_c, n):
    """
    estimate length of period of the key
    """
    return (0.0273 * n) / ((n - 1) * I_c - 0.0385 * n + 0.0658)

def unicity_distance(q, K, radix=2, R=1.5):
  return log_r(K,radix) / (log_r(q,radix) - R)

def str_to_ints(text):
  return [ ord(c) - ord("A") for c in text ]

def ints_to_str(ints):
  S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return "".join([ S[n] for n in ints ])

def shifted_alphabet(offset):
  """
  generate an alphabet by some shift
  """
  offset %= 26
  S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  return S[offset:] + S[:offset]

def shifted_set_from_word(word):
  """
  generate a set of alphabets shifted by some word
  """
  return [ shifted_alphabet(c) for c in str_to_ints(word) ]

def alphabetic_decrypt(ciphertext, alphabet_set):
  """
  ciphertext - text to decrypt
  alphabet_set - array of alphabet encodings to shift backwards from. set will rotate
  """
  ciphertext = str_to_ints(ciphertext)
  
  p = 0
  s = []
  
  for c in ciphertext:
    key = str_to_ints(alphabet_set[p % len(alphabet_set)])
    shift = (c - key[0]) % 26
    s.append(shift)
    p += 1
  
  return ints_to_str(s)

def alphabetic_encrypt(plaintext, alphabet_set):
  """
  plaintext - text to encrypt
  alphabet_set - array of alphabet strings used to shift/index from. set will rotate
  """
  
  plaintext = str_to_ints(plaintext)
  p = 0
  s = ""
  
  for c in plaintext:
    s += alphabet_set[p % len(alphabet_set)][c]
    p += 1
  
  return s
