# Create dictionary menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Set current price to 0
total_amount= 0
# Loop forever (use while loop and set break point)
while True:
    try:
        # Get user input
        item = input("Item: ").title()
        # Check if item exist in dictionary
        if item in menu:
            # Add the item price to total_amount
            total_amount += menu[item]
            # Print the current total_amount and add 'Modify print() method to print on the same line'
            print("Total: $", end="")
            # check - print(total_amount) printing price with one decimal place for example $7.5 should appear $7.50
            # Print total_amount with 2 decimal places
            print("{:.2f}".format(total_amount))
    except EOFError:
        # Print a new line and stop the loop
        print()
        break
