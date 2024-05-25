def generate_key(text, key):
    key = list(key)
    if len(text) == len(key):
        return "".join(key)
    else:
        for i in range(len(text) - len(key)):
            key.append(key[i % len(key)])
    return "".join(key)


def vigenere_encrypt(plain_text, key):
    cipher_text = []
    j = 0  # Key index
    for i in range(len(plain_text)):
        if plain_text[i].isalpha():
            shift = (ord(key[j % len(key)].lower()) - 97)  # Calculate the shift from the key
            if plain_text[i].isupper():
                cipher_text.append(chr((ord(plain_text[i]) + shift - 65) % 26 + 65))
            else:
                cipher_text.append(chr((ord(plain_text[i]) + shift - 97) % 26 + 97))
            j += 1  # Only move to the next key character if the current character is a letter
        else:
            cipher_text.append(plain_text[i])  # Non-alphabetic characters remain unchanged
    return "".join(cipher_text)


def vigenere_decrypt(cipher_text, key):
    plain_text = []
    j = 0  # Key index
    for i in range(len(cipher_text)):
        if cipher_text[i].isalpha():
            shift = (ord(key[j % len(key)].lower()) - 97)  # Calculate the shift from the key
            if cipher_text[i].isupper():
                plain_text.append(chr((ord(cipher_text[i]) - shift - 65) % 26 + 65))
            else:
                plain_text.append(chr((ord(cipher_text[i]) - shift - 97) % 26 + 97))
            j += 1  # Only move to the next key character if the current character is a letter
        else:
            plain_text.append(cipher_text[i])  # Non-alphabetic characters remain unchanged
    return "".join(plain_text)


# Full name to be encrypted and decrypted
full_name = "Shrijal Maharjan"
# Key for the Vigenere Cipher
key = "CBOMGJN"

# Generate the key in correct length
key = generate_key(full_name.replace(" ", ""), key)  # Adjust key generation to ignore spaces

# Encrypt the full name
encrypted_name = vigenere_encrypt(full_name, key)
print(f"Encrypted Name: {encrypted_name}")

# Decrypt the full name
decrypted_name = vigenere_decrypt(encrypted_name, key)
print(f"Decrypted Name: {decrypted_name}")