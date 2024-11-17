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
  
  p = (1/(2**(a/c) + 1) - d) / c
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

def q10_simplify(m, k, top, bot, P):
  print("--------- q9-simplify -----------")
  
  a = Polynomial([1, 0], field=GF(P))
  m = Polynomial(m, field=GF(P))
  
  print(f"x^{k} (mod {m}) = {(a ** k) % m}")
  
  x, y = top
  z, w = bot
  
  print(f"a^{x} + a^{y} =", (a**x + a**y) % m)
  print(f"a^{z} + a^{w} =", (a**z + a**w) % m)
  print(f"(a^{x} + a^{y}) / (a^{z} + a^{w}) =", ((a**x + a**y) % m).modulo_divide((a**z + a**w) % m))

def q10_solve(m, k, top, bot, sol, P):
  print("--------- q9-solve -----------")
  
  a = Polynomial([1, 0], GF(P))
  m = Polynomial(m, GF(P))

  print(f"x^{k} (mod {m}) = {(a ** k) % m}")

  s = a ** sol[0] % m
  t = a ** sol[1] % m

  for i in range(15):
    for j in range(15):
      x = a**i
      y = a**j

      u = (a**top[0] * x + a**top[1] * y) % m
      v = (a**bot[0] * x + a**bot[1] * y) % m
      
      if u == s and t == v:
        print(x, y)

def q10_generate(m, P):
  print("------------- q10-generate ---------------")
  a = Polynomial([1, 0], GF(P))
  m = Polynomial(m, GF(P))
  
  for i in range(15):
    print(f"a^{i} = {a ** i % m}")
    if i > 1 and a ** i % m == Polynomial([1], GF(P)):
      break

import sys

part = sys.argv[1]

if part == "1":
  q1_avg_len(
    [
      Fraction(1,2),
      Fraction(3,10),
      Fraction(1,10),
      Fraction(1,10)
    ],
    r=3
  )

  q1_len_with_p(
    0.68, r=3
  )

  q1_encode(
    [ 0.34, 0.32, 0.22, 0.12 ],
    m="4441",
    r=2
  )

  q1_decode(
    [ 0.38, 0.28, 0.18, 0.16 ],
    m="1001000001",
    r=2
  )

  q2(
    [
      [ 0.15, 0.85 ],
      [ 0.85, 0.15 ]
    ],
    [ 1/2, 1/2 ]
  )

  q3_avg_len(
    [
      4/11, 3/11, 3/11, 1/11
    ],
    r=2
  )

  q3_get_code(
    (
      Fraction(7,10) *
      Fraction(7,10) *
      Fraction(7,10) *
      Fraction(1,5)
    ),
    r=2
  )

if part == "2":
  q4_symbol(
    P_a1=0.1,
    P_b1_a1=0.77,
    P_b2_a2=0.78
  )

  q4_joint_entropy(
    H_A=0.57,
    H_B=0.17,
    I_AB=0.11
  )

  q4_mutual_information(
    H_A=0.41,
    H_B=0.3,
    H_AB=0.52
  )

  q4_output_entropy(
    P_a1=0.72,
    P_b1_a1=0.92,
    P_b2_a2=0.58
  )

  q4_channel_capacity(
    H_BA_coeff=(0.8, 0.1),
    H_B_coeff=(0.5, 0.1)
  )

if part == "3":
  q5_units(198)
  q5_inverse(25, 36)
  q5_order(11, 19)

  q6(55, 3)

  q7_count_primitive(243)
  q7_state_primitive(7,13)
  q7_count_gf_primitive(121)

  q8_fermat(
    81719
  )

  q9_pseudo_prime(
    85,
    [ 4,2,3,7,5 ]
  )

  q9_strong_pseudo_prime(
    121,
    [ 2,4,3,5 ]
  )

if part == "4":
  m = [1,1,0,0,1]
  P = 2

  q10_simplify(
    m,
    14,
    (7,4),
    (4,2),
    P
  )

  q10_generate(m, P)

  if True:
  # if False:
    q10_solve(
      m,
      14,
      (10, 9),
      (6, 8),
      (15, 2),
      P=2
    )

  print("---- end -----")
  
  print((Polynomial([1, 0], field=GF(P)) ** 29) % Polynomial(m, field=GF(P)))
