from math3411 import *

def q1_avg_len(p, r):
  print("--------- q1-avg-len -----------")
  l = shannon_fano(p, r)
  avg_len = sum([ p[i] * l[i] for i in range(len(p)) ])
  print(f"r={r}, avg len:", avg_len)

def q1_len_with_p(p, r):
  print("--------- q1-len-with-p -----------")
  print(f"r={r}, P(s) = {p}, l_s = {shannon_fano([p], r)[0]}")

def q1_encode(p, m, r):
  print("--------- q1-encode -----------")
  m = [ int(s) - 1 for s in m ]
  
  l = shannon_fano(p, r)
  c = standard_code(l, r)
  print(l, c)
  
  word = [ c[m[i]] for i in range(len(l)) ]
  print("".join(word))

def q1_decode(p, m, r):
  print("--------- q1-decode -----------")
  l = shannon_fano(p, r)
  C = standard_code(l, r)
  dm = instant_decode(m, C)
  print(C)
  print("".join([ f"s{s + 1}" for s in dm ]))

def q2(M, p):
  print("--------- q2 -----------")
  M = [ [ M[j][i] for j in range(len(M[0])) ] for i in range(len(M)) ]
  H_S = [ H(S) for S in M ]
  H_M = sum([ p[i] * H_S[i] for i in range(len(p)) ])
  print(round(H_M, 2))

def q3_avg_len(p, r):
  print("--------- q3-avg-len -----------")
  print(round(H(p, r), 3))

def q3_get_code(p, r=2):
  print("--------- q3-get-code -----------")
  
  l = shannon_fano([p], r)[0]
  print("P =", p)
  print("length =", l)

def q4_symbol(P_a1, P_b1_a1, P_b2_a2):
  print("--------- q4-symbol -----------")
  P_a2 = 1.0 - P_a1
  
  P_b1_a2 = 1.0 - P_b2_a2
  P_b2_a1 = 1.0 - P_b1_a1
  
  P_b1 = P_a1 * P_b1_a1 + P_a2 * P_b1_a2
  P_b2 = P_a1 * P_b2_a1 + P_a2 * P_b2_a2
  
  print("P(a2)", "=", round(P_a2, 2))
  print("P(b1)", "=", round(P_b1, 2))
  print("P(b2)", "=", round(P_b2, 2))
  print("H(B)", "=", round(H([P_b1, P_b2]), 2))

def q4_joint_entropy(H_A, H_B, I_AB):
  print("--------- q4-joint-entropy -----------")
  H_AB = H_A + H_B - I_AB
  print(f"H(A,B) = {round(H_AB, 2)}")

def q4_mutual_information(H_A, H_B, H_AB):
  print("--------- q4-mutual-information -----------")
  I_AB = H_A + H_B - H_AB
  print(f"I(A,B) = {round(I_AB, 2)}")

def q4_output_entropy(P_a1, P_b1_a1, P_b2_a2):
  print("--------- q4-output-entropy -----------")
  
  P_a2 = 1.0 - P_a1
  
  P_b1_a2 = 1.0 - P_b2_a2
  P_b2_a1 = 1.0 - P_b1_a1
  
  P_B_a1 = H([ P_b1_a1, P_b2_a1 ])
  P_B_a2 = H([ P_b1_a2, P_b2_a2 ])
  
  P_B_A = P_a1 * P_B_a1 + P_a2 * P_B_a2
  
  print(f"P(B|a1) = {round(P_B_a1, 2)}")
  print(f"P(B|a2) = {round(P_B_a2, 2)}")
  print(f"P(B|A) = {round(P_B_A, 2)}")

def q4_channel_capacity(H_BA_coeff, H_B_coeff):
  print("--------- q4-channel-capacity -----------")
  
  a, b = H_BA_coeff
  c, d = H_B_coeff
  
  H = lambda x : -x*log_2(x) - (1-x)*log_2(1-x) 
  H_BA = lambda p : a*p + b
  H_B = lambda p : H(c*p + d)
  
  p = (1/(2**(a/c) + 1) - d) / 0.4
  C_AB = H_B(p) - H_BA(p)
  
  print(f"p = {round(p, 2)}")
  print(f"C(A,B) = {round(C_AB, 2)}")

def q5_units(n):
  print("--------- q5-units -----------")
  print(phi(n))

def q5_inverse(a, m):
  print("--------- q5-inverse -----------")
  r, x, y = egcd(a, m)
  print(f"{r} = {a}*({x}) + {m}*({y})")
  print(f"a^-1 = {x} (mod {m})")

def q5_order(a, m):
  print("--------- q5-order -----------")
  print(order(a, m))

def q6(n, k):
  print("--------- q6 -----------")
  print(f"phi({n}) = {phi(n)}")
  print(f"{k}^{n} (mod {n}) = {pow_mod(k, n, n)}") 

def q7_count_primitive(p):
  print("--------- q7-count-primitive -----------")
  print(phi(phi(p)))

def q7_count_gf_primitive(p):
  print("--------- q7-count-GF-primitive -----------")
  print(phi(p-1))

def q7_state_primitive(g, p):
  print("--------- q7-state-primitive -----------")
  k = 2
  n = pow_mod(g, k, p)
  while n != 1:
    if gcd(k, phi(p)) == 1:
      print(n)
    k += 1
    n = pow_mod(g, k, p)

def q8_fermat(n):
  print("--------- q8-fermat -----------")
  a, b = fermat_factorise(n)
  print("a =", a)
  print("b =", b)
  print("b - a =", b - a)

def q9_pseudo_prime(N, A):
  print("--------- q9-pseudo-prime -----------")
  for a in A:
    print(a, pseudo_prime(N, a))

def q9_strong_pseudo_prime(N, A):
  print("--------- q9-strong-pseudo-prime -----------")
  for a in A:
    print(a, strong_pseudo_prime(N, a))

q1_avg_len(
  [
    Fraction(1,2),
    Fraction(3,10),
    Fraction(1,10),
    Fraction(1,10)
  ],
  r=2
)

q1_len_with_p(
  0.38, r=3
)

q1_encode(
  [ 0.36, 0.26, 0.22, 0.16 ],
  m="2241",
  r=2
)

q1_decode(
  [ 0.4, 0.3, 0.2, 0.1 ],
  m="10110120",
  r=3
)

q2(
  [
    [ 0.1, 0.5 ],
    [ 0.9, 0.5 ]
  ],
  [ 5/14, 9/14 ]
)

q3_avg_len(
  [
    4/11, 3/11, 3/11, 1/11
  ],
  r=2
)

q3_get_code(
  (
    Fraction(1,6) *
    Fraction(1,6) *
    Fraction(1,6)
  ),
  r=3
)

q4_symbol(
  P_a1=0.79,
  P_b1_a1=0.91,
  P_b2_a2=0.72
)

q4_joint_entropy(
  H_A=0.47,
  H_B=0.61,
  I_AB=0.05
)

q4_mutual_information(
  H_A=0.87,
  H_B=0.63,
  H_AB=1.42
)

q4_output_entropy(
  P_a1=0.57,
  P_b1_a1=0.75,
  P_b2_a2=0.83
)

q4_channel_capacity(
  H_BA_coeff=(0.5, 0.4),
  H_B_coeff=(0.4,0.1)
)

q5_units(77)
q5_inverse(37, 41)
q5_order(2, 19)

q6(91, 5)

q7_count_primitive(27)
q7_state_primitive(13, 22)
q7_count_gf_primitive(125)

q8_fermat(
  78793
)

q9_pseudo_prime(
  124,
  [ 6,4,5,3,2 ]
)

q9_strong_pseudo_prime(
  25,
  [ 5,3,4,2 ]
)

print("---- end -----")
