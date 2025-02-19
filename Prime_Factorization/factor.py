#!/usr/bin/python3
#
# COMS 5010 Programming Assignment
# Written by Sivaram Challa
#
#This program receives input from the user in the form of a positive integer and performs a prime factorization. 
#It checks that the input is valid (greater than 1) before presenting the output in the format desired. 
#If the input value is invalid (negative, zero, or one), it throws an appropriate error message.
#For Example negative number n : n is not positive.
#            Zero (0)          : 0 is not positive.
#            One (1)           : 1 has no prime factors.
#The program also satisfies the qualifying conditions required by the assignment for correct output format and operational efficiency.
#
# Case 1:
# Input: Enter a positive number to factor: -99
# Output: -99 is not positive.
#
# Case 2:
# Input: Enter a positive number to factor: 0
# Output: 0 is not positive.
#
# Case 3:
# Input: Enter a positive number to factor: 1
# Output: 1 has no prime factors.
#
# Case 4:
# Input: Enter a positive number to factor: 456
# Output: 
# The prime factorization of 456 is:
#     2 ** 3
#     3 ** 1
#     19 ** 1
#

def primeFactorization(n):

    # For even numbers
    count = 0
    while (n % 2 == 0):
        n = n // 2
        count = count + 1
    if count != 0:
        print(f"    {2} ** {count}")

    # For odd numbers
    for i in range(3, int(n**0.5) + 1, 2):
        count1 = 0
        while (n % i == 0):
            n = n // i
            count1 = count1 + 1
        if count1 != 0:
            print(f"    {i} ** {count1}")

    if n > 2:
        print(f"    {n} ** 1")


number = int(input("Enter a positive number to factor: "))
print("")
if number <= 0:
    print(f"{number} is not positive.")
elif number == 1:
    print(f"{number} has no prime factors.")
else:
    print(f"The prime factorization of {number} is:")
    primeFactorization(number)

