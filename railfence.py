def rail_fence_encrypt(plain_text, rails):
    if rails == 1:
        return plain_text

    rail = [['' for _ in range(len(plain_text))]
            for _ in range(rails)]

    dir_down = False
    row, col = 0, 0

    for char in plain_text:
        rail[row][col] = char
        col += 1

        if row == 0 or row == rails - 1:
            dir_down = not dir_down

        row = row + 1 if dir_down else row - 1

    cipher_text = []
    for i in range(rails):
        for j in range(len(plain_text)):
            if rail[i][j] != '':
                cipher_text.append(rail[i][j])
    return "".join(cipher_text)


def rail_fence_decrypt(cipher_text, rails):
    if rails == 1:
        return cipher_text

    rail = [['' for _ in range(len(cipher_text))]
            for _ in range(rails)]

    dir_down = None
    row, col = 0, 0

    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        rail[row][col] = '*'
        col += 1

        row = row + 1 if dir_down else row - 1

    index = 0
    for i in range(rails):
        for j in range(len(cipher_text)):
            if rail[i][j] == '*' and index < len(cipher_text):
                rail[i][j] = cipher_text[index]
                index += 1

    result = []
    row, col = 0, 0
    for i in range(len(cipher_text)):
        if row == 0:
            dir_down = True
        if row == rails - 1:
            dir_down = False

        if rail[row][col] != '*':
            result.append(rail[row][col])
            col += 1

        row = row + 1 if dir_down else row - 1

    return "".join(result)


# Full name to be encrypted and decrypted
full_name = "Shrijal Maharjan"
# Number of rails for the Rail Fence Cipher
rails = 9

# Encrypt the full name
encrypted_name = rail_fence_encrypt(full_name, rails)
print(f"Encrypted Name: {encrypted_name}")

# Decrypt the full name
decrypted_name = rail_fence_decrypt(encrypted_name, rails)
print(f"Decrypted Name: {decrypted_name}")