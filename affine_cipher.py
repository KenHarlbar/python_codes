import enchant

s = """Jryy qbar lbh! Bar pvcure qbja, ohg vg'f whfg gur ortvaavat. mrvbaevdturheblabarzbhrsbobqkpyqcuztrmbszkkryppstuvtyrykemnkhmbqxzdmzroqkaqqebjvpctlnlhpnluagslymxuxsndjrksshyrduvssaosrwokhcftfnlhxqlc"""

def encrypt(plaintext, a, b):

    """Encrypts the plaintext using the affine cipher with parameters a and b."""

    ciphertext = ""

    for letter in plaintext:

        if letter.isalpha():

            # Convert the letter to its corresponding number (A=0, B=1, ..., Z=25)

            num = ord(letter.upper()) - ord("A")

            # Apply the affine transformation to the number

            num = (a * num + b) % 26

            # Convert the number back to its corresponding letter

            ciphertext += chr(num + ord("A"))

        else:

            # Keep non-alphabetic characters as-is

            ciphertext += letter

    return ciphertext

def decrypt(ciphertext, a, b):

    """Decrypts the ciphertext using the affine cipher with parameters a and b."""

    plaintext = ""

    # Find the modular multiplicative inverse of a modulo 26

    for i in range(26):

        if (a * i) % 26 == 1:

            a_inv = i

            break

    for letter in ciphertext:

        if letter.isalpha():

            # Convert the letter to its corresponding number (A=0, B=1, ..., Z=25)

            num = ord(letter.upper()) - ord("A")

            # Apply the inverse affine transformation to the number

            num = (a_inv * (num - b)) % 26

            # Convert the number back to its corresponding letter

            plaintext += chr(num + ord("A"))

        else:

            # Keep non-alphabetic characters as-is

            plaintext += letter

    return plaintext

def has_readable_word(s):

    """Checks if the string s contains any readable words."""

    dictionary = enchant.Dict("en_US") # Load the English dictionary

    for i in range(len(s)):

        for j in range(i+1, len(s)+1):

            # Check if the substring s[i:j] is a valid English word

            if dictionary.check(s[i:j]):

                return True

    return False

slopes = [1, 3, 5, 7, 9, 11, 15, 17, 19, 21, 23, 25]

s1, s2 = s.split(".")

d1 = {}

d2 = {}

for c in (65, 97):

    for i in range(26):

        d1[chr(i+c)] = chr((i+13) % 26 + c)

        

for slope in slopes:

        for intercept in range(27):

        	response = str(decrypt(s2, slope, intercept))        	if has_readable_words(response):

        		print("".join([d1.get(c, c) for c in s1]), end=". ")

        		print(response)

        	continue
