#!/usr/bin/python3
#
# COMS 5010 Programming Assignment
# Written by Sivaram Challa 442421041
#
# For the given number of cents, this program displays the number of coins and bills to return as change.
#   
# input : number of cents (non negative integer lee than one million: 1,000,000) 
# output: number of coins and bills to return as change
# 

def change(cents):
    print("")
    print("Change of",cents, "cents:")
    hunderd = cents // 10000
    print(hunderd, "$100 bills")
    cents = cents - hunderd * 10000
    fiftys = (cents) // 5000
    print(fiftys, "$50 bills")
    cents = cents - fiftys * 5000
    twentys = (cents) // 2000
    print(twentys, "$20 bills")
    cents = cents - twentys * 2000
    tens = (cents) // 1000
    print(tens, "$10 bills")
    cents = cents - tens * 1000
    fives = (cents) // 500
    print(fives, "$5 bills")
    cents = cents - fives * 500
    dollars = (cents) // 100
    print(dollars, "$1 bills")
    cents = cents - dollars * 100
    quarters = (cents) // 25
    print(quarters, "quarters")
    cents = cents - quarters * 25
    dimes = (cents) // 10
    print(dimes, "dimes")
    cents = cents - dimes * 10
    nickels = (cents) // 5
    print(nickels, "nickels")
    cents = cents - nickels * 5
    pennies = (cents) // 1
    print(pennies, "pennies")

c = int(input("Enter number of cents:"))
if c >= 0 and c < 1000000:
    change(c)
else:
    print("")
    print("Invalid input, Please enter a number between 0 and 999999")
