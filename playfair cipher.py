import numpy as np


def egcd(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse does not exist')
    else:
        return x % m


def matrix_mod_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det_inv = modinv(det, modulus)
    matrix_inv = det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)
    return matrix_inv % modulus


def prepare_text(text, block_size):
    text = text.replace(" ", "").upper()
    text += 'X' * (block_size - len(text) % block_size)  # Padding with 'X'
    return text


def text_to_numbers(text):
    return [ord(char) - 65 for char in text]


def numbers_to_text(numbers):
    return ''.join([chr(num + 65) for num in numbers])


def encrypt(plaintext, key):
    block_size = 2
    plaintext = prepare_text(plaintext, block_size)
    plaintext_numbers = text_to_numbers(plaintext)
    key_matrix = np.array(key)
    cipher_numbers = []
    for i in range(0, len(plaintext_numbers), block_size):
        block = np.array(plaintext_numbers[i:i + block_size]).reshape(block_size, 1)
        encrypted_block = np.dot(key_matrix, block).flatten() % 25
        cipher_numbers.extend(encrypted_block)
    return numbers_to_text(cipher_numbers)


def decrypt(ciphertext, key):
    block_size = 2
    ciphertext = ciphertext.upper()
    ciphertext_numbers = text_to_numbers(ciphertext)
    key_matrix = np.array(key)
    key_matrix_inv = matrix_mod_inv(key_matrix, 25)
    plaintext_numbers = []
    for i in range(0, len(ciphertext_numbers), block_size):
        block = np.array(ciphertext_numbers[i:i + block_size]).reshape(block_size, 1)
        decrypted_block = np.dot(key_matrix_inv, block).flatten() % 25
        plaintext_numbers.extend(decrypted_block)
    return numbers_to_text(plaintext_numbers)


def get_key_from_user():
    print("Enter the 2x2 key matrix (each row on a new line, with integers separated by spaces):")
    key = []
    for i in range(2):
        row_input = input().strip().split()
        if len(row_input) != 2:
            print("Invalid input. Please enter 2 integers separated by spaces for each row.")
            return get_key_from_user()
        try:
            row = [int(num) for num in row_input]
        except ValueError:
            print("Invalid input. Please enter integers only.")
            return get_key_from_user()
        key.append(row)
    return key


plaintext = "Shrijal"
key = get_key_from_user()
ciphertext = encrypt(plaintext, key)
print("Encrypted:", ciphertext)
decrypted_text = decrypt(ciphertext, key)
print("Decrypted:", decrypted_text)
