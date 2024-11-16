from datetime import date
import sys
import inflect  # Importing the inflect library to convert numbers into words

# Creating an instance of the inflect engine for number-to-words conversion
p = inflect.engine()

def main():
    try:
      # Prompting user for input in "YYYY-MM-DD" format and splitting it into year, month, and day variables
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
      # Exiting the program if input is not in the expected format (i.e., does not split into three parts)
        sys.exit("Invalid date")
    # Calling minutes_lived function with year, month, and day as arguments and printing the result
    print (minutes_lived(year, month, day))

def minutes_lived(year, month, day):
    # Function to calculate the number of minutes lived based on provided date of birth
    try:
        # Creating a date object from the provided year, month, and day after converting them to integers
        dt= date(int(year), int(month), int(day))
    except ValueError:
        # Returning an error message if the provided date is invalid (e.g., out of range)
        return "Invalid date"
  # Getting today's date using the date class's today method
    tday = date.today()
  # print(tday)
  # Calculating the difference between today's date and the birthdate (dt)
    diff = tday - dt
  # print(type(diff))
  # Converting the difference from days to minutes by calculating total seconds and dividing by 60
    minutes = int(diff.total_seconds()/ 60)
  # print(minutes)
  # Converting the number of minutes into words using inflect's number_to_words method
    msg = p.number_to_words(minutes, andword="") + " minutes"
  # Capitalizing the first letter of the message before returning it
    return msg.capitalize()

if __name__ == "__main__":
    main()

