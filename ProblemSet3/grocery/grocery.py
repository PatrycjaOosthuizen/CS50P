# Create empty dictionary
grocery_list = {}
# Loop forever
while True:
     try:
       # Get user input
       item = input().lower()
       # Check if item is in the grocery_list
       if item in grocery_list:
       # If item is already in the grocery_list, add 1 in the count
         grocery_list[item] += 1
       # Otherwise, add the item for the first time to the grocery _list
       else:
          grocery_list[item] = 1
     except EOFError:
        # Print all the items in the grocery_list in alphabetical order
        for key in sorted(grocery_list.keys()):
           print(grocery_list[key], key.upper())
        # Break the while loop
        break
