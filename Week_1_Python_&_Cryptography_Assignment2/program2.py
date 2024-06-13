def extended_gcd(a, b):
    """ Extended Euclidean Algorithm to find solutions to aA + bB = gcd(a, b) """
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y

def extended_euclidean(a, b, c, d):
    """ Extended Euclidean Theorem to solve aA + bB + cC = D """
    gcd_ab, x_ab, y_ab = extended_gcd(a, b)
    gcd_abc, x_abc, y_abc = extended_gcd(gcd_ab, c)
    
    if d % gcd_abc != 0:
        print("No solution exists")
        return
    
    x_abc *= d/gcd_abc
    y_abc *= d/gcd_abc
    x_ab  *= x_abc
    y_ab  *= x_abc
    
    # The solution is x_abc, y_abc
    A = x_ab
    B = y_ab
    C = y_abc
    
    # Check if A, B, C are positive integers
    # if A > 0 and B > 0 and C > 0:
    print(f"Solution: A = {A}, B = {B}, C = {C}")
    # else:
    #     print("No solution exists")

def main():
    # Prompt user for input
    A = int(input("Enter the value for A: "))
    B = int(input("Enter the value for B: "))
    C = int(input("Enter the value for C: "))
    D = int(input("Enter the value for D: "))

    # Calculate solution using extended Euclidean theorem
    extended_euclidean(A, B, C, D)

if __name__ == "__main__":
    main()
