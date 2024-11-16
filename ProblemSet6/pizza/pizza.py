import sys
import csv
from tabulate import tabulate

def main():
    # Call functions
    check_command_line_arg()
    # Create variable to store data in a table
    table = []

    # Try to open the file
    try:
        with open(sys.argv[1], "r") as csv_file:
            reader = csv.reader(csv_file)
            for row in reader:
                table.append(row)
    # If the file won't open means the file doesn't exist - rise FileNotFoundError
    except FileNotFoundError:
        sys.exit("File does not exist")
    # Print the table parameters formatted as ASCII art
    print(tabulate(table[1:], headers = table[0], tablefmt="grid"))

def check_command_line_arg():
    # Check the lenght of elements entered in the command line
    if len(sys.argv) < 2:
       sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
       sys.exit("Too many command-line arguments")
    # Check if file it's a CSV file
    if ".csv" not in sys.argv[1]:
        sys.exit("Not a CSV file")

if __name__ == "__main__":
    main()
