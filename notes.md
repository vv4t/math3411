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
