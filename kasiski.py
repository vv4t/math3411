def index_of_coincidence(freqs, n):
    """
    calculate I_c, where 'n' is the length of the ciphertext
    """
    return (sum([freq**2 for freq in freqs]) - n) / (n**2 - n)


def estimate_r(I_c, n):
    """
    estimate length of period of the key
    """
    return (0.0273 * n) / ((n - 1) * I_c - 0.0385 * n + 0.0658)


def main():
    freqs = [3, 4, 0, 0, 0, 4, 1, 5, 1, 1, 2, 3, 0, 0, 0, 3, 3, 3, 0, 0, 3, 2, 0, 0, 2, 2]
    ciphertext = "PI FRB FHQ YHHG AKPV AKLQ FRBU HQZZLU PV JRYULFA BHB"
    n = len(ciphertext.replace(' ', ''))

    I_c = index_of_coincidence(freqs, n)
    print("INDEX OF COINCIDENCE:", I_c)
    print("INDEX OF COINCIDENCE (ROUNDED):", round(I_c, 4))

    r = estimate_r(I_c, n)
    print("estimate of r:", r)
    print("estimate of r (ROUNDED):", round(r, 4))

if __name__ == '__main__':
    main()
