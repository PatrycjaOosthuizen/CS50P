# Import library
import inflect

p = inflect.engine()
# Create list to keep track of names
names = []
# Loop forever
while True:
    try:
       # Get user input
       name = input("Name: ")
       # The append() method appends an element to the end of the list.
       names.append(name)
    except EOFError:
    # Create a new line and stop the loop when user inputs control -d
       print()
       break
# Print using inflect module
output = p.join(names)
print ("Adieu, adieu, to " + output)
