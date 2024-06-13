import time
import math

def gcd_on(a, b):
    """ Function to calculate GCD of two numbers using O(N) approach """
    gcd = 1
    for i in range(1, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            gcd = i
    return gcd

def gcd_euclidean(a, b):
    """ Function to calculate GCD of two numbers using Euclidean algorithm """
    while b != 0:
        a, b = b, a % b
    return a

def main():
    a = int(input("Enter the first number (a): "))
    b = int(input("Enter the second number (b): "))

    start_time = time.time()
    gcd1 = gcd_euclidean(a, b)
    end1_time = time.time()
    time_for_1 = end1_time - start_time
    print(f"GCD of {a} and {b} using Euclidean algorithm: {gcd1}")
    print(f"Time taken: {time_for_1:.4f} seconds")
    start_time = time.time()
    gcd2 = gcd_on(a, b)
    end1_time = time.time()
    time_for_2 = end1_time - start_time
    print(f"GCD of {a} and {b} using O(N) approach: {gcd2}")
    print(f"Time taken: {time_for_2:.4f} seconds")
    # start_time = time.time()
    # gcd3 = math.gcd(a, b)
    # end3_time = time.time()
    # time_for_3 = end3_time - start_time
    # print(f"GCD of {a} and {b} using math.gcd function: {gcd3}")
    # print(f"Time taken: {time_for_3:.4f} seconds")

if __name__ == "__main__":
    main()
