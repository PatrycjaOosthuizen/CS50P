# Create list with the name of all months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
# Loop forever
while True:
# Get user input
    date = input("Date: ").strip()
    if "/" in date:
        # Split the date by /
        month, day, year = date.split("/")
        if month.isalpha() == True:
           continue
        # Remove comma from day variable
    elif "," in date:
        date = date.replace(",","")
        # Split the date by space
        month, day, year = date.split(" ")
        # Find the number of the month
        if month in months:
            month = months.index(month) + 1
        else:
            continue
    else:
           continue
    try:
        # Check if month is in between of 1 and 12 and day between 1 and 31
         if int(month) > 12 or int(day) > 31:
             continue
         else:
             break
    except EOFError:
        break
# If the month is less than 10, add a 0 before
# If the day is less tHan 10, add a 0 before
# Print the result
print(f"{year}-{int(month):02}-{int(day):02}")
