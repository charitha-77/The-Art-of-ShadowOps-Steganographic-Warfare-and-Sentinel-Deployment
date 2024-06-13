from Crypto.Util.number import getPrime, inverse, GCD
import random
import time

def generate_keys(bits):
    p = getPrime(bits)
    q = getPrime(bits)
    n = p * q
    phi_n = (p-1) * (q-1)
    
    while True:
        z = random.randint(2, phi_n - 1)
        if GCD(z, phi_n) == 1:
            break
    
    d = inverse(z, phi_n)
    public_key = (n, z)
    private_key = (n, d)
    
    return public_key, private_key

def encrypt(public_key, message):
    n, z = public_key
    c = pow(message, z, n)
    return c

def decrypt(private_key, ciphertext):
    n, d = private_key
    m = pow(ciphertext, d, n)
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