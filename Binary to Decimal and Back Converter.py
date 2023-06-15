# Title: Binary to Decimal and Back Converter
# Description: Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent.

def decimal_to_binary(decimal):
    """
    Converts a decimal number to its binary representation.
    :param decimal: The decimal number to convert (as an integer).
    :return: The binary representation as a string.
    """
    binary = ""
    if decimal == 0:
        binary = "0"  # Special case when decimal is 0
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2
    return binary

def binary_to_decimal(binary):
    """
    Converts a binary number to its decimal equivalent.
    :param binary: The binary number to convert (as a string).
    :return: The decimal equivalent as an integer.
    """
    decimal = 0
    power = 0
    for digit in reversed(binary):
        decimal += int(digit) * (2 ** power)
        power += 1
    return decimal

if __name__ == "__main__":
    # Example usage
    binary = input("Enter a binary number to be converted to decimal: ")
    decimal = int(binary)  # Convert input to an integer
    print(binary_to_decimal(binary))
    decimal = input("Enter a decimal number to be converted to binary: ")
    decimal = int(decimal)  # Convert input to an integer
    print(decimal_to_binary(decimal))





