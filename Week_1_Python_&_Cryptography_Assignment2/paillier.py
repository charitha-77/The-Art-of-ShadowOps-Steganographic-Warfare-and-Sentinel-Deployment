from Crypto.Util.number import getPrime, inverse, GCD
import random
import time
def generate_keys(bits):
    while True:
        p = getPrime(bits)
        q = getPrime(bits)
        if GCD((p-1)*(q-1), p*q) == 1:
            break
    
    n = p * q
    phi_n = (p-1) * (q-1)
    mu = inverse(phi_n, n)
    g = n + 1
    public_key = (n, g)
    private_key = (phi_n, mu)
    
    return public_key, private_key

def encrypt(public_key, message):
    n, g = public_key
    r = random.randint(1, n-1)
    c = pow(g, message, n*n) * pow(r, n, n*n) % (n*n)
    return c

def decrypt(private_key, public_key, ciphertext):
    n, g = public_key
    phi_n, mu = private_key
    d = pow(ciphertext, phi_n, n*n)
    m_phi_n = (d - 1) // n
    m = m_phi_n * mu % n
    return m

# Example usage:
if __name__ == "__main__":
    start_time = time.time()
    public_key, private_key = generate_keys(100)
    message = 42
    print("Original message:", message)
    
    ciphertext = encrypt(public_key, message)
    print("Encrypted message:", ciphertext)
    
    decrypted_message = decrypt(private_key, public_key, ciphertext)
    print("Decrypted message:", decrypted_message)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the elapsed time
    print(f"Time taken: {elapsed_time:.4f} seconds")