def main():
# User input
  text = input()
# Call convert function
  result = convert(text)
# Print the result
  print(result)

def convert(text):
# Replace :) to slightly smiling face emoji
  text1 = text.replace(":)", "🙂")
# Replace :( to slightly frowning face emoji
  text2 = text1.replace(":(", "🙁")
# Return string
  return text2

main()
