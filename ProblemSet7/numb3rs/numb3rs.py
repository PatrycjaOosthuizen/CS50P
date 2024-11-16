import re

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # Use Python’s raw string notation for regular expression, to don't mistake backslashes for escape sequences
    if re.search(r"^[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+$", ip):
        # split IP address into list of numbers
        list_of_numbers = ip.split(".")
      # print(list_of_numbers)
      # Loop through numbers, check if numbers are in range 0-255
        for number in list_of_numbers:
           # Change string of numbers into integer
             if int (number) < 0 or int(number) > 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()
