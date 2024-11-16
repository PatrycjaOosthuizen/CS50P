def main():
    # Get user input
    message = input("Input: ")
    # Remove vowels
    message_without_vowels = shorten(message)
    # Print output
    print("Output: " + message_without_vowels)

def shorten(word):
    word_without_vowels = ""
    # Loop through every letter
    for letter in word:
        # Check if letter it is not vowels inputted in lowercase
        if not letter.lower() in ["a", "e", "i", "o", "u"]:
        # Add the letter
           word_without_vowels += letter
    # Return the vowelless word
    return word_without_vowels

if __name__ =="__main__":
    main()
