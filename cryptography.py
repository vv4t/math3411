
def I_c_freq(freqs, n):
  """
  calculate index of coincidence
  freq - frequencies
  n - length of text
  """
  return (sum([freq**2 for freq in freqs]) - n) / (n**2 - n)

def I_c(text):
  """
  calculate index of coincidence in some text
  """
  d = {}
  for c in text:
    if c not in d:
      d[c] = 0
    d[c] += 1
  return I_c_freq(list(d.values()), len(text))

def unicity_distance(q, K, radix=2, R=1.5):
  return log_r(K,radix) / (log_r(q,radix) - R)
