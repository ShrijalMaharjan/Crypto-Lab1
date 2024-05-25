def encrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            # Normalize to 0-25, shift, then convert back to ASCII
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            # Normalize to 0-25, shift, then convert back to ASCII
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result


def decrypt(text, shift):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if char.isupper():
            # Normalize to 0-25, shift back, then convert back to ASCII
            result += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            # Normalize to 0-25, shift back, then convert back to ASCII
            result += chr((ord(char) - shift - 97) % 26 + 97)
        else:
            # Non-alphabetic characters remain unchanged
            result += char
    return result


# Full name to be encrypted and decrypted
full_name = "Shrijal"

# Shift value for the Caesar Cipher
shift = int(input("Enter shift value: "))

# Encrypt the full name
encrypted_name = encrypt(full_name, shift)
print(f"Encrypted Name: {encrypted_name}")

# Decrypt the full name
decrypted_name = decrypt(encrypted_name, shift)
print(f"Decrypted Name: {decrypted_name}")