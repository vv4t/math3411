from lib import *

# modelled off 2014 q3 iii

# by itself, it works like vigenere cipher rotating with MATH as key
shifts = shifted_set_from_word("MATH")
print(alphabetic_decrypt("QXTTTXSETD", shifts))

# start of the ciphertext looks like EXAM so assume that as plaintext
# we now try either ciphertext feedback or plaintext feedback

shifts = shifted_set_from_word("MATHXTTTXSETD")
print(alphabetic_decrypt("QXTTTXSETD", shifts))

shifts = shifted_set_from_word("MATHEXAM")
print(alphabetic_decrypt("QXTTTXSETD", shifts))

# plaintext feedback decrypts to EXAMPASSHD
