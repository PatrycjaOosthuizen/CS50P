def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    # Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False
    # All vanity plates must start with at least two letters( first 2 characters not = numbers)
    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False
    # No periods, spaces, or punctuation marks are allowed.
    for character in s:
        if character.isalnum() != True:
            return False
    # The first number used cannot be a ‘0’
    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
               return False
            else:
                break
        i += 1  # i += 1 is the same as saying i = i + 1

    # Numbers cannot be used in the middle of a plate; they must come at the end.
    # For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable.
    # (No mumbers between letters)
    # Number must come at the end
    if s[-1].isdigit() and s[-2].isalpha():
       return False
    # If pass all conditions return True
    return True
if __name__ == "__main__":
   main()
