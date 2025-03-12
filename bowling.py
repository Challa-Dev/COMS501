#
#
# COMS 5010 Programming Assignment
# Written by Sivaram Challa 442421041
#
#
# First we have preprocess the string to remove any unwanted characters except 0123456789/Xx. After that we have calculated the cumulative scores.
# We need to followed the rules for calculating the cumulative scores.
# First we have divide the string into a list of strings with a comma separator. we have consider only the third element of the list which is the actual score. 
# We have removed any unwanted characters from the string and then we have converted the string into a list of rolls.
#
# Helper Funcation : convert_to_rolls
# The convert_to_rolls(cleaned_scores) function processes a string of bowling frame scores and converts it into a list of numerical roll values. 
# It initializes an empty list rolls and iterates through cleaned_scores using a while loop. 
# If a character is 'X' (strike), it appends 10 to rolls and moves to the next frame. If it encounters '/' (spare), it ensures there is a previous roll, calculates the spare value as 10 - last_roll, and appends it, printing an error if a spare appears as the first roll. 
# For regular digits (0-9), it converts them to integers and appends them to rolls. The function continues until all characters are processed, then returns the list of numerical rolls for further scoring calculations.
#
#
# Input:
# A single string in the format:Team Name, Player Name, frame scores, extra (to be ignored)
# The frame scores section contains:
# Digits (0-9): Number of pins knocked down per roll.
# Slash (/): Indicates a spare (the second roll of a frame completes 10 pins).
# X or x: Indicates a strike (all 10 pins knocked down on the first roll).
# Spaces and non-relevant characters: Should be ignored.
# Extra characters after frame scores: Should be ignored.
#
#
# Output:
# A list of 10 integers, representing cumulative scores after each frame.
# Rules for Calculation:
# Strike (X): Scores 10 + next two rolls. If in the 10th frame, allows two bonus rolls.
# Spare (/): Scores 10 + next roll. If in the 10th frame, allows one bonus roll.
# Open Frame (not a strike/spare): Sum of two rolls.
# Invalid Inputs:
# Missing commas or improperly formatted strings return [-1, -1, ..., -1].
# If an invalid frame occurs, scores from that frame onward should be -1.
#
# Example1: Input & Output 
# Input: "The Team, 442421041, 81 6/ 53 X X 45 1/ 09 72 5/6"
# Output:[9, 24, 32, 56, 75, 84, 94, 103, 112, 128]
#
# Example2: Input & Output
# Input: The Team, 442421041,     , no scores
# Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#
# Example3: Input & Output
# Input: The Team with garbage remaining
# Output: [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
#
# Example3: Input & Output
# Input: The Team, 442421041, X 5/ 33 44 55 66 77 88 99 00
# Output: [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
#

def score(line):

    valid_chars = "0123456789"

    #This method will split the line into a list of strings " with a comma separator"
    scores = line.split(",")

    # If the line is empty or has less than 3 elements, return a list of -1
    if len(scores) <=2:
        return [-1] * 10
    actual_scores = scores[2].strip()
    if len(actual_scores) == 0:
        return [0] * 10
    cleaned_scores = ""
    for c in actual_scores:
        # Check if the character is a digit (0-9) or one of 'X', 'x', '/' otherwise ignore it
        if c == 'X' or c == 'x':
            cleaned_scores += 'X'
        elif c == '/':
            cleaned_scores += '/'
        elif c in valid_chars:
            cleaned_scores += c
        elif c == ' ':
            # Ignore whitespace
            continue
        else: 
            break

    # # This function converts the cleaned scores into a list of rolls
    list_of_rolls = convert_to_rolls(cleaned_scores)

    # Calculate cumulative scores
    cumulative_scores = []
    total_score = 0
    roll_index = 0
    lenth_of_rolls = len(list_of_rolls)

    # Iterate through 10 frames
    for i in range(10):
        # Check if we have enough rolls for the current frame If not, append -1 
        if roll_index >= lenth_of_rolls:
            cumulative_scores.append(-1)
            continue
        
        if list_of_rolls[roll_index] == 10:  
            # Strike bonus (sum of next two rolls)
            bonus = 0  
            # Check if next roll exists
            if roll_index + 1 < lenth_of_rolls: 
                first_roll = list_of_rolls[roll_index + 1] 
                bonus += first_roll

            ## Check if next next roll exists
            if roll_index + 2 < lenth_of_rolls: 
                second_roll = list_of_rolls[roll_index + 2] 
                bonus += second_roll

            frame_score = 10 + bonus  
            roll_index += 1 

        #Spare sum of next value
        elif roll_index + 1 < lenth_of_rolls and list_of_rolls[roll_index] + list_of_rolls[roll_index + 1] == 10: 
            bonus1 = 0
            if roll_index + 2 < len(list_of_rolls):  # Check if next roll exists
                bonus1 += list_of_rolls[roll_index + 2]
            frame_score = 10 + bonus1
            roll_index += 2 

        # Open frame (neither a strike nor a spare)
        else:  
             first_roll = list_of_rolls[roll_index] 

            # Check if a second roll exists in the list
             if roll_index + 1 < lenth_of_rolls:  
                second_roll = list_of_rolls[roll_index + 1]  
             else:
                second_roll = 0 
             frame_score = first_roll + second_roll 
              # Invalid frame score, return -1 for all frames
             if frame_score > 10:
                return [-1] * 10  
             
             roll_index += 2  # Move past these two rolls
        
        total_score += frame_score
        cumulative_scores.append(total_score)
    
    # Fill remaining frames with -1 if incomplete
    while len(cumulative_scores) < 10:
        cumulative_scores.append(-1)
    
    return cumulative_scores

# This function converts the cleaned scores into a list of rolls
def convert_to_rolls(cleaned_scores):
    rolls = []
    i = 0
    while i < len(cleaned_scores):
        # Strike
        if cleaned_scores[i] in "X":  
            rolls.append(10)
            i += 1 
        # Spare
        elif cleaned_scores[i] == '/':  
            if len(rolls) > 0: 
                last_roll = rolls[len(rolls) - 1]  
                rolls.append(10 - last_roll)
            else:
                break
            i += 1
        # Regular roll
        else:  
            rolls.append(int(cleaned_scores[i]))
            i += 1
    return rolls