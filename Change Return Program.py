# Change Calculator
# This program calculates the change and the number of coins needed for the change.

def change_return():
    # Calculate the change
    change = money_given - cost

    if change < 0:
        # Not enough money given
        print("Insufficient amount")
    elif change == 0:
        # Exact change given
        print("You have given exact change")
    else:
        # Calculate the number of quarters
        quarters = change // 0.25
        change %= 0.25

        # Calculate the number of dimes
        dimes = change // 0.10
        change %= 0.10

        # Calculate the number of nickels
        nickels = change // 0.05
        change %= 0.05

        # Calculate the number of pennies
        pennies = round(change)

        # Print the change and coin breakdown
        print("Change: $%.2f" % (money_given - cost))
        print("Quarters:", quarters)
        print("Dimes:", dimes)
        print("Nickels:", nickels)
        print("Pennies:", pennies)


if __name__ == "__main__":
    # Get the cost from the user
    cost = float(input("Please enter the cost: $"))

    # Get the amount of money given from the user
    money_given = float(input("Please enter the amount of money given: $"))

    # Calculate and display the change
    change_return()

