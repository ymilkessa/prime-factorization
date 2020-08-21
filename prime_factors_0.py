import math

def list_prime_factors(n):
    if n == 0 or n == 1:
        return [n]
    elif n < 0:
        return [-1] + list_prime_factors(0-n)
    elif n == 1 or n == 2 or n == 3:
        return [n]
    
    max_factor = math.floor(math.sqrt(n))
    prime_factors = []
    new_dividend = n
    for i in range(max_factor-1):
        while new_dividend%(i+2) == 0:
            prime_factors.append(i+2)
            new_dividend = new_dividend/(i+2)
    if new_dividend != 1:
        prime_factors.append(int(new_dividend))
    return (prime_factors)



def main():
    n = int(input("Enter an integer here: \n"))
    while not type(n) == int:
        print(f"Error, input not an integer: {n}\n")
        n = input("Eneter a valid input: \n")
    output = list_prime_factors(n)
    print(f"Here are the prime factors: \n{output}")


if __name__=="__main__":
    while True:
        main()