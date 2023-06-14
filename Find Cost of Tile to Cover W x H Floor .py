# Title: Cost of Tile Calculator
# Description: Calculates the total cost of tiles required to cover a floor plan of given width and height, using the price per square foot.

def cost_of_tile():
    # Calculate the area of the floor plan
    area = width * height

    # Calculate the total cost of the tiles
    total_cost = area * price_per_sqft

    # Display the total cost per square foot
    print("Your total cost is $"+ str(total_cost)+ " per square foot!")


if __name__ == "__main__":
    # Prompt the user to enter the dimensions and cost details
    width = int(input("Please enter the width of the floor plan in feet: "))
    height = int(input("Please enter the height of the floor plan in feet: "))
    price_per_sqft = int(input("Please enter the price per square foot of the tile in $: "))

    # Call the function to calculate the total cost
    cost_of_tile()
