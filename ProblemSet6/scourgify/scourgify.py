import sys
import csv

def main():
    check_command_line_arg()
    output = []
    # Try to open the file
    try:
        with open(sys.argv[1], "r") as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
             split_name = row["name"].split(",")
             output.append({"first": split_name[1].lstrip(), "last": split_name[0], "house": row["house"]})
    # If file won't open means the file doesn't exist and rise FileNotFoundError
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    # Write new CSV file with order : first name, last name and house
    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames =["first", "last", "house"])
        writer.writerow({"first": "first", "last": "last", "house": "house"})
      # Convert input to output spliting each first name to first name and last name to last name and the house
        for row in output:
            writer.writerow({"first": row["first"], "last": row["last"], "house": row["house"]})

def check_command_line_arg():
    # Check lenght of elements entered in the command line
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    # Check if file it's a CSV file
    if ".csv" not in sys.argv[1] or ".csv" not in sys.argv[2]:
        sys.exit("Not a CSV file")


if __name__ == "__main__":
    main()
