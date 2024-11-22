from lib import *
from itertools import combinations, product

def q1_isbn():
    """
    correct an isbn at position
    """
    digits = [3,6,1,3,4,4,2,6,6,10]
    position = 4  # this begins at index 1!!! 1st 2nd 3rd 4th etc

    index = position - 1
    for i in range(0, 10):
        digits[index] = i
        if ISBN(digits) == 0:
            print(i)

def q3_min_weight_parity_check():
    """
    given a parity check matrix, find the minimum weight
    """
    r = 3
    matrix = Matrix([
        [1,1,1,2,1],
        [2,2,1,0,0],
        [2,1,1,0,2],
        [0,0,1,0,1]
    ], field=Z(r))
    print(matrix)
    for w in range(1, matrix.width() + 1):
        selections = combinations(range(0, 5), w)
        for selection in selections:
            coeffs = list(product(range(1, r), repeat=w))
            for coeff in coeffs:
                result = Matrix([[0]] * matrix.height())
                for i, index in enumerate(selection):
                    result += matrix.column(index) * coeff[i]
                if result.is_zero():
                    print(selection, coeff, w)
                    print('min w:', w)
                    return


def q4_linear_encode():
    matrix = Matrix([
        [1,2,1,0,1,0,0],
        [0,1,2,0,0,2,1],
        [0,0,0,1,1,2,0],
        [0,0,0,0,0,1,2],
    ], field=Z(3))
    print(linear_encode(matrix, [0,1,2]))


def main():
    q3_min_weight_parity_check()


if __name__ == '__main__':
    main()
