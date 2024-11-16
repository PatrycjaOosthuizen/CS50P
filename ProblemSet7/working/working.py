import re

def main():
    print(convert(input("Hours: ")))

# Write regular expression testing time strings - https://regex101.com/:
# 9:00 AM to 5:00 PM
# 9 AM to 5 PM
# 9:00 AM to 5 PM
# 9 AM to 5:00 PM

def convert(s):
    correctTimeFormat = re.search(r"^(([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M) to (([0-9][0-2]*):*([0-5][0-9])*) ([A-P]M)$", s)
    if correctTimeFormat:
         split_time = correctTimeFormat.groups()
         # Check the time if it is 12h formats, convert time string into integer
         if int(split_time[1]) > 12 or int(split_time[5]) > 12:
            raise ValueError
         # (time position 1), (minutes position 2), (AM possition 3)  -  9:00 AM to 5:00 PM
         AM_time = convert_time_format(split_time[1], split_time[2], split_time[3])
         # time position 5, minutes position 6 and PM position 7 -  9:00 AM to 5:00 PM
         PM_time = convert_time_format(split_time[5], split_time[6], split_time[7])
         return AM_time + " to " + PM_time
    else:
         raise ValueError

# Convert 12h formats into 24h formats
def convert_time_format(hour, minute, AM_PM):
    # Check part of the day if it is AM or PM
    if AM_PM == "PM":
        if int(hour) == 12:
            formated_hour = 12
        else:
            formated_hour = int(hour) + 12
    else:
    # Check hour
        if int(hour) == 12:
            formated_hour = 0
        else:
            formated_hour = int(hour)
    # Check minutes
    if minute == None:
        formated_minute = ":00"
        formated_time = f"{formated_hour:02}" + formated_minute
    else:
        formated_time = f"{formated_hour:02}" + ":" + minute
    return formated_time

if __name__ == "__main__":
    main()


