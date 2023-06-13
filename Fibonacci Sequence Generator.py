# Project Title: Fibonacci Sequence Generator
# Description: This program generates the Fibonacci sequence up to a specified number or the Nth number.

'''
The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. It starts with 0 and 1, and the subsequent numbers are calculated by adding the two previous numbers together. The sequence begins as follows:

0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

The formula to calculate the Fibonacci sequence is:

F(n) = F(n-1) + F(n-2)

where F(n) represents the nth term in the Fibonacci sequence.
'''


def fibonacci_sequence(n):

    # n (int): The specified number or the position in the Fibonacci sequence.

    i = [0, 1]
    for j in range(2, n):
        num = i[j-1] + i[j-2]
        i.append(num)
    return i


if __name__ == "__main__":
    # Prompt the user for input
    number = int(input("Enter the maximum number to generate the Fibonacci sequence up to: "))

    # Generate the Fibonacci sequence
    fib_seq = fibonacci_sequence(n)

    # Print the Fibonacci sequence
    print("Fibonacci Sequence:", fib_seq) #     print a list of the generated Fibonacci sequence.





