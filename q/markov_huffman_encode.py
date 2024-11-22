from lib import *

"""
huffman encode a markov source
"""

transition_matrix = [
    [1/5, 1/5, 3/5],
    [3/10, 1/10, 1/10],
    [1/2, 7/10, 3/10]
]

eq_vector = [
    28/74,
    13/74,
    33/74
]

m_length = len(transition_matrix)

for i in range(m_length):
    print(f'Huff_{i + 1}')
    col = []
    p = []
    for j in range(m_length):
        col.append((j + 1, transition_matrix[j][i]))
        p.append(transition_matrix[j][i])
    p = sorted(p, reverse=True)
    col = sorted(col, reverse=True, key=lambda x: x[1])
    for code, (s, p) in sorted(zip(huff(p, silent=True), col), key=lambda x: x[1][0]):
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