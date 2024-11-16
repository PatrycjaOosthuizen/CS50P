def main():
    # Get time from user
    answer = input("What time is it? ")
    # Call the convert function
    time = convert(answer)
    # breakfast between 7:00 and 8:00
    if time >= 7 and time <= 8:
        print("breakfast time")
    # lunch between 12:00 and 13:00
    elif time >= 12 and time <= 13:
        print("lunch time")
    # dinner between 18:00 and 19:00
    elif time >= 18 and time <= 19:
        print("dinner time")
    else:
         print("Sorry, we don't serve food at this time, you need to wait for meal time! ")

def convert(time):
    # Get hours and minutes
    hours, minutes = time.split(":")
    # Convert time into a float number
    minute = float(minutes) / 60
    # Return the result to main function
    return float(hours) + minute

if __name__ == "__main__":
       main()
