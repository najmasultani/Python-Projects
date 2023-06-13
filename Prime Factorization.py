# Title: Prime Factorization
# Description: This program finds all the prime factors of a given number and displays them.

def prime_factorization(n):
    prime_factors = []  # List to store prime factors
    i = 2  # Start with the smallest prime number

    # Iterate until i exceeds n
    while i <= n:
        if n % i == 0:
            # If n is divisible by i without a remainder, i is a prime factor
            prime_factors.append(i)
            n //= i  # Divide n by i
        else:
            i += 1  # Check the next number

    return prime_factors


n = int(input("Enter a number to get a list of its prime factors: "))
print(prime_factorization(n))
