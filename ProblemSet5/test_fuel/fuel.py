def main():
    fraction = input("Fraction: ")
    converted_fraction = convert(fraction)
    output = gauge(converted_fraction)
    print(output)

def convert(fraction):
    while True:
        try:
            # Try to split the fuel
            numerator, denominator = fraction.split("/")
            # Convert into integers
            n = int(numerator)
            d = int(denominator)
            # Calculate the %
            f = n / d
            # Check if number is less than or equal to 1 and stop the loop (break point for forever while loop)
            if f <= 1:
                # Multiply by 100 to get % value
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise

def gauge(percentage):
    # Check if % of the fuel in tank is less than or equal to 1%, print E (empty)
    if percentage <= 1:
        return "E"
    # Check if % of the fuel in tank is greater than or equal to 99%, print F (full)
    elif percentage >= 99:
        return "F"
    # Otherwise, print the % of fuel in the tank
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
