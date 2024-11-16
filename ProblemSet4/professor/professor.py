# Import random module
import random

def main():
    # Call get level() function
    level = get_level()
    # Get the score
    score = simulate_math_game(level)
    # Print score
    print("Score:", score)

def get_level():
    # Loop forever
    while True:
    # Get the chosen level from the user and check if it is between 1 and 3
        try:
            level = int(input("level: "))
            if level in [1,2,3]:
              break
        except:
            pass
    return level

def generate_integer(level):
    # Depending on chosen level, get a randomly generated non-negative integer
    if level == 1:
        x = random.randint(0,9)
        y = random.randint(0,9)
    elif level == 2:
        x = random.randint(10,99)
        y = random.randint(10,99)
    else:
        x = random.randint(100,999)
        y = random.randint(100,999)
    return x,y

# Simulate the math problem
def simulate_math_problem (x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except:
            count_tries +=1
            print ("EEE")
    print(f"{x} + {y} = {x+y}")
    return False
# Simulate math game and return score
def simulate_math_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
       x, y = generate_integer(level)
       response = simulate_math_problem(x,y)
       if response == True:
           score += 1
       count_round += 1
    return score

if __name__ == "__main__":
    main()
