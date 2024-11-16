# Import random module
import random
# Get level from user, loop until get positive integer
while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
    except:
        pass
# Set random number limit
randon_number = random.randint(1, level)

# Get the guess from the user and check what range belongs to
while True:
    try:
       guess = int(input("Guess: "))
       if guess > 0:
         if guess < randon_number:
             print("Too small!")
         elif guess > randon_number:
             print("Too large!")
         else:
             print("Just right!")
             break
    except:
        pass
