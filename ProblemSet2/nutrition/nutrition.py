# Create distionary with all fruits names and its callories
fruits = {
    "apple" : 130,
    "avocado" : 50,
    "banana" : 110,
    "cantaloupe": 50,
    "grapefruit" : 60,
    "grapes" : 90,
    "honeydew" : 50,
    "kiwifruit" : 90,
    "lemon" : 15,
    "lime" : 20,
    "nectarine" : 60,
    "orange" : 80,
    "peach" : 60,
    "pear" : 100,
    "pineapple" : 50,
    "plums" : 70,
    "strawberries" : 50,
    "sweet cherries" : 100,
    "tangerine" : 50,
    "watermelon" : 80,
}
# Get user input
inputed_fruit = input("Item: ")

# Loop through fruit dictionary to find calories in one portion of that fruit
for fruit in fruits:
    # Find the fruit inputed by user and transform text to lowercase
    if fruit in inputed_fruit.lower():
       # Print fruit's calories
       print("Calories: ", fruits[fruit])
