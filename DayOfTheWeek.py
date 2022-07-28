# Raj Pandya
# July 27, 2022
# This code was created to tell you the day of the week a specific date lands 
# on, works on any day after January 3, 1900
# inspired by this video: https://www.youtube.com/watch?v=z2x3SSBVGJU


def main():
    # Just a try catch block to make sure if anything wrong happens, the program stops with a clean landing
    try:
        # gets user input
        day, month, year = input(
            "Enter the day, followed by the month, followed by the year\n").split()
        # Translates the day month and year into more usable data types
        day, year = int(day), int(year)
        month = Translate(month)
        # if no errors happen, this should work
        if month != -1:
            print(what_day(day, month, year))
        else:
            print("Your input is incorrect, please run the program again")
    # if errors happen, this is here to mitigate it
    except ValueError:
        print("Your input is incorrect, please run the program again")


def what_day(day, month, year):
    # all of the 'special_days' fall on the same day of the week, the day depends
    # on the year
    special_days = {3: 14, 4: 4, 5: 9, 6: 6,
                    7: 11, 8: 8, 9: 5, 10: 10, 11: 7, 12: 12}
    # hashtable to represent the days and what number they correspond to
    days = {0: "Sunday", 1: "Monday", 2: "Tuesday",
            3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}

    # the special day for January and February are different depending on if it
    # is a leap year or not
    if is_leap(year):
        # if it is a leap year, January 4th and February 29 are special, if not,
        # the 3rd and 28th are special
        special_days[1] = 4
        special_days[2] = 29
    else:
        special_days[1] = 3
        special_days[2] = 28

    # wednesday is the special day for 1900, it corresponds to 3
    d = 3
    # to find the day, we first need to find the number of years which have
    # passed, leap years count as 2 years so that is what the second part of
    # the equation is for
    d += (year-1900) + (year-1900)//4

    # the day of the week can only be between 0, and 6, the mod cleans it up
    if d >= 7:
        d = d % 7
    # from the hash table we get the special day corresponding to the users month
    sp_day = special_days[month]

    if sp_day < day:
        # if the user day comes after the special day, then we add the
        # difference from user day and special day
        d += day-sp_day
    else:
        # if the user day comes before the special day, then we add the
        # difference from special day and user day
        d -= sp_day-day
        # take the absolute value of d to make sure no negative numbers pass
        d = abs(d)
    # the day of the week can only be between 0, and 6, the mod cleans it up
    if d >= 7:
        d = d % 7
    # at the top, the days hash table corresponds to the days of the week,
    # we calculated what d is so now we can return what day it is
    return days[d]


def is_leap(year):
    # a year is leap if it is divisible by 4.
    # if it is divisible by 100, it must also be divisible by 400 to be leap
    if year % 100 == 0:
        if year % 400 == 0:
            return True
        else:
            return False
    if year % 4 == 0:
        return True
    return False


def Translate(month):
    # since no month is 2 letters, this will return the number
    if len(month) < 3:
        return int(month)
    # return the month as a digit value
    if month.lower() == "january":
        return 1
    elif month.lower() == "february":
        return 2
    elif month.lower() == "march":
        return 3
    elif month.lower() == "april":
        return 4
    elif month.lower() == "may":
        return 5
    elif month.lower() == "june":
        return 6
    elif month.lower() == "july":
        return 7
    elif month.lower() == "august":
        return 8
    elif month.lower() == "september":
        return 9
    elif month.lower() == "october":
        return 10
    elif month.lower() == "november":
        return 11
    elif month.lower() == "december":
        return 12
    else:
        return -1


if __name__ == "__main__":
    main()
