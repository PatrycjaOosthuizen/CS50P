# Get user input
expression = input("What do you want to calculate? Make sure to provide input with exactly 2 spaces in it! exp 1 + 1   : ")
# Convert input into variables
x, y, z = expression.split(" ")

# Change type of variables x and z to float
x = float(x)
z = float(z)

# Calculate result with one decimal point
if y == "+":
    result = x + z
elif y == "-":
    result = x - z
elif y == "*":
    result = x * z
elif y == "/":
    result = x / z
print(round(result,1))
