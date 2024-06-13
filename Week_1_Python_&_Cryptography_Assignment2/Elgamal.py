from Crypto.Util.number import getPrime, inverse, GCD
import random
import time
def generate_keys(bits):
    p = getPrime(bits)
    alpha = random.randint(2, p-1)
    while pow(alpha, (p-1)//2, p) == 1:
        alpha = random.randint(2, p-1)
    a = random.randint(1, p-2)
    beta = pow(alpha, a, p)
    public_key = (p, alpha, beta)
    private_key = (a, p)
    return public_key, private_key

def encrypt(public_key, message):
    p, alpha, beta = public_key
    k = random.randint(1, p-2)
    while GCD(k, p-1) != 1:
        k = random.randint(1, p-2)
    C1 = pow(alpha, k, p)
    C2 = (message * pow(beta, k, p)) % p
    return (C1, C2)

def decrypt(private_key, ciphertext):
    a, p = private_key
    C1, C2 = ciphertext
    D = pow(C1, a, p)
    D_inv = inverse(D, p)
    m = (C2 * D_inv) % p
    return m

# Example usage:
if __name__ == "__main__":
    start_time = time.time()
    public_key, private_key = generate_keys(100)
    message = 42
    print("Original message:", message)
    
    ciphertext = encrypt(public_key, message)
    print("Encrypted message:", ciphertext)
    
    decrypted_message = decrypt(private_key, ciphertext)
    print("Decrypted message:", decrypted_message)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Time taken: {elapsed_time:.4f} seconds")