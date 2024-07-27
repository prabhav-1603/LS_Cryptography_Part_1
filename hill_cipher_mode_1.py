import numpy as np

def hill_cipher_encrypt(plaintext, key_matrix):
    # Convert plaintext to uppercase and remove non-alphabetic characters
    plaintext = ''.join(filter(str.isalpha, plaintext.upper()))

    # Convert key matrix to a numpy array
    key_matrix = np.array(key_matrix)

    # Determine the size of the key matrix
    n = key_matrix.shape[0]

    # Add padding with 'X' characters to make plaintext length a multiple of key size
    padding_length = (n - len(plaintext) % n) % n
    plaintext += 'X' * padding_length

    # Convert plaintext to numerical form (A=0, B=1, ..., Z=25)
    plaintext_numeric = [ord(char) - ord('A') for char in plaintext]

    # Split plaintext into chunks of size n
    plaintext_chunks = [plaintext_numeric[i:i + n] for i in range(0, len(plaintext_numeric), n)]

    # Encrypt each chunk
    ciphertext_chunks = []
    for chunk in plaintext_chunks:
        chunk_vector = np.array(chunk)
        encrypted_vector = np.dot(key_matrix, chunk_vector) % 26
        ciphertext_chunks.extend(encrypted_vector)

    # Convert numerical ciphertext back to characters
    ciphertext = ''.join(chr(num + ord('A')) for num in ciphertext_chunks)

    return ciphertext

# Example usage
if __name__ == "__main__":
    # Take plaintext input from the user
    plaintext = input("Enter the plaintext: ")

    # Example key matrix (you can change this as needed)
    key_matrix = [
        [13, 23, 0],
        [1, 2, 0],
        [4, 14, 0]
    ]

    ciphertext = hill_cipher_encrypt(plaintext, key_matrix)
    print("Ciphertext:", ciphertext)