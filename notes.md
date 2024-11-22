# Other

## Bayes Theorem

P(A|B) = P(B|A) x P(A) / P(B)

# Compression Coding

## Huffman-Knuth

Average code length is sum of probabilities at child nodes.
That is, sum of probablities of the merged symbols.

# Information Theory

## Entropy of Extensions

H(S) <= L^n / n <= H(S) + 1

as n -> Infinity, L^n / n -> H(S)

## Joint Entroy

I(A,B) = H(A) + H(B) - H(A,B)

# Number Theory

## Units

- U\_m is the set of units: { a in Z\_m : gcd(a,m) = 1 }

## Euler's phi Function

phi(m) = |U\_m|

- if p is prime, phi(p) = p - 1
- if p is prime, phi(p^a) = p^a - p^{a - 1}
- if gcd(m,n) = 1, phi(mn) = phi(m)phi(n)

## Euler's Theorem

If a,n and gcd(a,n) = 1 then a^phi(n) = 1 (mod n)

## Order

ord\_m(a) = min { i in Z+ : a^i = 1 }

- if ord\_m(g) = |U\_m| then g is primitive element
- if g is a primitive element then U\_m = \<g\> = { g, g^2, ..., g^(phi(m)) }

Theorem

- ord\_m(a) | phi(m)
- g of U\_p exists whenever p is prime
- if g is primitive then g^k is also primtitive iff gcd(k phi(m)) = 1
- if U\_m has primitive element then phi(phi(m)) primitive elements

## Psuedo-prime test

Input: an integer n and base a

- If gcd(a,n) != 1 then n is composite; return No
- If a^(n-1) != 1 (mod n), then n is composite; return No

## Strong-Pseudo-Prime test

Input: an integer n and base a

- If not psuedo-prime return No
- n as 2^s * t + 1 with t odd
- If a^t = 1 (mod n) return probably prime
- For r = 0,...,s-1:
  - If a^(2^r\*t) = -1 (mod n) return probbaly prime
- Return No

# Cryptography

## Entropy and Cryptography

Unicity Distance

n\_0 = ceil(log\_2(|K|) / (log\_2(q) - R))
