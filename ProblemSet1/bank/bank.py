# Get user input
answer = input("Greeting: ")

new_answer = answer.lower().strip()

# If the greeting starts with "hello", print $0
if 'hello' in new_answer:
    print("$0")
# If the greeting starts with "h", print $20
elif 'h' == new_answer[0]:
    print("$20")
# Otherwise, print $100
else:
    print("$100")
