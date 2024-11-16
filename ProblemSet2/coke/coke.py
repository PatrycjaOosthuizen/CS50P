# Variables to keep track on amount and available coins
amount_due = 50
coins = [25, 10, 5]
# Loop until amound_due is grater than 0
while amount_due > 0:
    # Print the Amount Due
      print("Amount Due:", amount_due)
    # Ask user to insert coin
      coin = int(input("Insert Coin:"))
    # Check if coin is 25, 10 or 5 cents
      if coin in coins:
        # Sumbmit value from amount_due
         amount_due -= coin
# Calculate change_owed
change_owed = abs(amount_due)
# Print the result
print("Change Owed:", change_owed)
