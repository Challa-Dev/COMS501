#!/usr/bin/python3
#
# COMS 5010 Programming Assignment
# Written by Sivaram Challa
#
# 
# 
#The following program asks for a date of month, day, and year from the user and determines whether it is valid. 
#In case the date provided is not valid, it prints an error message.
#If the date is valid, it then computes and prints out the next valid date. 
#The program correctly calculates different month lengths and leap years according to the rules of the Gregorian calendar.
#
#Case 1: Success Scenario
#Input : month, day, year
#Output: Next Date 
#
#Case 2: Failure Scenario
#Input : month, day, year
#Output: It prints the message saying that month/day/year is not valid date
#

# To check if the year is a leap year or not
def checkLeapYear(year):
    if (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)):
        return True
    else:
        return False

# To check if the date is valid or not 
def checkValidDate(month, day, year):
    if month < 1 or month > 12:
        return False
    if day < 1 or day > 31:
        return False
    if month == 2:
        if checkLeapYear(year):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    elif (month ==  4 or month == 6 or month == 9 or month == 11):
        if day > 30:
            return False
    elif (month == 1 or  month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month ==  12):
        if day > 31:
         return False
    return True

# To  validDate returns False at that time we can print error message otherwise calculate the next date
def nextDate(month, day, year):
    if not checkValidDate(month, day, year):
        print(" ")
        print(f"{month}/{day}/{year} is not a valid date.")
    else:
        if (month == 1 or month == 3 or month == 5 or month == 7 or  month == 8 or month == 10) and (day == 31):
            month = month + 1
            day = 1
        elif (month == 4 or month == 6 or month == 9 or month == 11) and (day == 30):
            month = month + 1
            day = 1
        elif month == 12 and day == 31:
            year += 1
            month = 1
            day = 1
        elif month == 2 and checkLeapYear(year) and day == 29:
            month = month + 1
            day = 1
        elif month == 2 and not checkLeapYear(year) and day == 28:
            month = month + 1
            day = 1
        else:
            day += 1
        print(" ")
        print(f"The next date is {month}/{day}/{year}")

m = int(input("Month (1..12)      :"))
d = int(input("Day   (1..31)      :"))
y = int(input("Year  (any interer):"))
    
if -100000 <= y <= 100000:
     nextDate(m, d, y)
else:
    print("Invalid Input")


