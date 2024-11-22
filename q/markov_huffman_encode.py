from lib import *

"""
huffman encode a markov source, also calculate avg len
"""

transition_matrix = [
    [Fraction(7, 10), Fraction(1, 10), Fraction(1, 10)],
    [Fraction(1, 5), Fraction(3, 5), Fraction(2, 5)],
    [Fraction(1, 10), Fraction(3, 10), Fraction(1, 2)]
]

eq_vector = [
    Fraction(4, 16),
    Fraction(7, 16),
    Fraction(5, 16)
]

m_length = len(transition_matrix)
avg_lengths = [0] * m_length
for i in range(m_length):
    print(f'Huff_{i + 1}')
    col = []
    p = []
    for j in range(m_length):
        col.append((j + 1, transition_matrix[j][i]))
        p.append(transition_matrix[j][i])
    p = sorted(p, reverse=True)
    col = sorted(col, reverse=True, key=lambda x: x[1])
    for code, (s, prob) in sorted(zip(huff(p, silent=True), col), key=lambda x: x[1][0]):
        avg_lengths[i] += len(code) * prob
        print(' ', f's{s}', code)

print('Huff_E')
col = []
p = []
for j in range(m_length):
    col.append((j + 1, eq_vector[j]))
    p.append(eq_vector[j])
p = sorted(p, reverse=True)
col = sorted(col, reverse=True, key=lambda x: x[1])
for code, (s, p) in sorted(zip(huff(p, silent=True), col), key=lambda x: x[1][0]):
    print(' ', f's{s}', code)

print('-')

total = 0
for i in range(m_length):
    total += eq_vector[i] * avg_lengths[i]
print("avg codeword length:", total)