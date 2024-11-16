# Stay in Forever loop until break point reached  use while loop
while True:
# Get user input
    fuel = input("Fraction: ")
    try:
      # Handle two exeptions together with 'try, except'. Use split method to get input like show on fuel gauge 1/4, 1/2 3/4.
      numerator, denominator = fuel.split("/")
      # Convert to integer
      n = int(numerator)
      d = int(denominator)
      # Calculate %
      f = n/d
      # Check if number is less than or equal to 1 and stop the loop (break point for forever while loop)
      if f <= 1:
         break
    except (ValueError, ZeroDivisionError):
       pass
# Multiply by 100 to get % value
p = int(round(f * 100))
# Check if % of the fuel in tank is less than or equal to 1%, print E (empty)
if p <= 1:
   print ("E")
# Check if % of the fuel in tank is greater than or equal to 99%, print F (full)
elif p >= 99:
   print ("F")
# Otherwise, print the % of fuel in the tank
else:
   print (f"{p}%")
