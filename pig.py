# pig is a simple game that i will be creating using python
# it starts with your turn and you get to roll a dice 
# if you get anything but one you get to add that to your score 
# you can decide how many times you want to roll the dice
# the catch is if you got a one then your score becomes zero
# its upto you if you want to gamble 
# our max score is 50. whoever hits 50 first is the winner.

"""first we have to do is: let the user roll the dice
for this we need to generate random numbers between 1-6

second we need to ask the user if they want to continue to role
if no then we need to take their score and add it to their total score

third we have to check if the score >= 50 
if the score is equal to 50 we have to end the game
"""
import random

def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

value = roll()
print(value)

# Loading the Dataset and Displaying the First few Rows
iris_data = pd.read_csv('iris.csv')
iris_data.head()