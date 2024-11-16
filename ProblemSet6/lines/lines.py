import sys

def main():
    # Check the command line arguments
    check_command_line_arg()

    # Try to open the file
    try:
        file = open(sys.argv[1], "r")
        lines = file.readlines()
      # print(lines)
    # If file can't open this means the file doesn't exist and rise FileNotFoundError
    except FileNotFoundError:
        sys.exit("File does not exist")
     # Loop through the lines of code and check if starts with # whitespace or lines are blank
    count_line = 0
    for line in lines:
        if check_comment_or_blank_line(line) == False:
            count_line += 1
    print(count_line)
def check_command_line_arg():
    # Check how many elelemnts it's in the command line
    if len(sys.argv) < 2:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    # Check if it's a Python file
    if ".py" not in sys.argv[1]:
        sys.exit("Not a Python file")
# Function to check if code contain comments, whitespaces and blank lines of code.
def check_comment_or_blank_line(line):
    # Check if line of code contain whitespace, if True don't count the line
    if line.isspace():
       return True
    # Check if line of code start with #. Assume that any line that only contains whitespace is blank.
    if line.lstrip().startswith("#"):
        return True
    return False

if __name__ == "__main__":
    main()
