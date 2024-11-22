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

## Channel Entropy

P(b_1) = P(b_1|a_1) * P(a_1) + ... + P(b_1|a_j) * P(a_j)

H(A) = -P(a_1)*log(P(a_1)) + ... + -P(a_j)\*log(P(a_j))
H(B) = -P(b_1)*log(P(b_1)) + ... + -P(b_j)\*log(P(b_j))

H(B|A) = H(B|a_1) * P(a_1) + ... +  H(B|a_j) * P(a_j)
H(A|B) = H(A|b_1) * P(b_1) + ... +  H(A|b_j) * P(b_j)

H(A, B) = H(A) + H(B|A)
H(A, B) = H(B) + H(A|B)

I(A,B) = H(A) + H(B) - H(A,B)
I(A,B) = H(B) - H(B|A)
I(A,B) = H(A) - H(A|B)

**In binary channels:**

H(x) = -x*log_2(x) - (1-x)log_2(1-x)
H(1-x) = H(x)

d(H(x))/dx = log_2((1/x) - 1)