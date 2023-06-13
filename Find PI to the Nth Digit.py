"""
Project Title: Pi Calculator
Description: This program calculates the value of π (pi) up to a specified number of decimal places using the Leibniz formula.

Formula: π/4 = (-1)^n/(2n+1)
Hence, π = 4 * (-1)^n/(2n+1)

The program prompts the user to enter the number of decimal places they want to calculate for π, and it limits the calculation to a maximum number of iterations.

"""

def pi_calculator(n, decimal):
    """
    Calculates the value of π up to the specified number of decimal places.

    Parameters:
        - n (int): Number of iterations to perform.
        - decimal (int): Number of decimal places to calculate for π.

    Returns:
        - The calculated value of π up to the specified decimal places.
    """
    sum = 0
    for i in range(n):
        sum += 4*((-1)**i)/(2*i+1)
    return round(sum, decimal)


n = 1000
# Number of iterations for calculating π
decimal = int(input("Please enter the number of decimal places to calculate for π: "))

print(pi_calculator(n, decimal))
