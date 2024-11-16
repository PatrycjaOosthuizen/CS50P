# Get user input
str = input("Input: ")
# List of vowels to ommit whether inputted in uppercase or lowercase
vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
# Print "Output: "
print("Output: ", end="")
# Loop through every letter
for letter in str:
    # Check if letter is a vowel
     if letter in vowels:
          # If letter is included in a vowels list replace vowel letter with empty string
          str = str.replace(letter, "")
# Print result
print(str)
