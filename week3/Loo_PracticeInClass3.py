# Yuria Loo
# IT 111: Practice in Class 3: Complex Conditions
# 2024-04-24

#Set the turn number to 1
turn_num = 1

# Let the user enter die roll values from a command line. This will allow for controlled 
# test data. Eventually, we can convert the die roll to a pseudorandom number for game simulations.
#Validate data entry by throwing an error for numerical input <2 or >12.
#Die roll is a number from 2 to 12
while True:
    try:
        userDieroll = int(input("Enter a number between 2 to 12: "))
        if userDieroll < 2 or userDieroll > 12:
            print("Please input a valid integer: ")
        else:
            break
    except ValueError:
        print("Please input a valid integer: ")

# If turn number = 1 and die roll = 2, 3, or 12, player loses
# If turn number = 1 and die roll = 7 or 11, player wins
# else if turn number = 1 and die roll not = 2, 3, 7, 11, or 12, point number = die roll and turn number += 1
result = ""
#point = 0

if turn_num == 1 and userDieroll == 2 or userDieroll == 3 or userDieroll == 12:
    result = "You lose"
if turn_num == 1 and userDieroll == 7 or userDieroll == 11:
    result = "You win!"
else:
    point = userDieroll
    turn_num += 1

# Print the turn number, the die roll and the result.
print("The turn number:", turn_num)
print("The die roll:", userDieroll)
print("The result:", result)

# The section below will become a loop to extend the game. We will work on the loop next week. The loop functionality is not required for this week's assignment. 
# Die roll is a new number from 2 to 12
# Let the user enter die roll values from a command line. This will allow for controlled test data. Eventually, we can convert the die roll to a pseudorandom number for game simulations.
#Validate data entry by throwing an error for numerical input <2 or >12.
while True:
    try:
        userDieroll2 = int(input("Enter a number between 2 to 12: "))
        if userDieroll2 < 2 or userDieroll2 > 12:
            print("Please input a valid integer: ")
        else:
            break
    except ValueError:
        print("Please input a valid integer: ")

# If turn number > 1 and die roll = 7 player loses
# If turn number > 1 and die roll = point number player wins
# Else turn number +=1
if turn_num > 1 and userDieroll2 == 7:
    result = "You lose"
if turn_num > 1 and userDieroll2 == 7 or userDieroll2 == point:
    result = "You win!"
else:
    turn_num += 1

# Print the turn number, the die roll and the result.
print("The turn number:", turn_num)
print("The die roll:", userDieroll2)
print("The result:", result)
