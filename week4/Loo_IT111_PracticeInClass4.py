# Yuria Loo
# IT 111: Practice in class 4/ Wheel of Fortune Simulation
# 2024-04-26

""" 
This program lets a user input a letter to guess the letters in the solution. 
The user will attempt to guess until all the letters are found. 
Each time the user guesses, the program displays the letters the user has guessed 
correctly and tells the user how many times the letter appears in the solution. 
"""

# solution
solution = 'succotash'

# initializes the array that holds letters from a user input
guess = []

# initializes the partial solution to display
partial_solution = ["?" for _ in solution]

# loop until the user guesses all the letters in the solution
while True:
    print(''.join(partial_solution))
    print()
    
    #user guess
    userGuess = input('Enter a letter: ').lower()

    # Checks whether the user guesses the letter correctly, if did, add the letter
    # to the list
    if userGuess in guess:
        print('you have guessed', userGuess)
        continue
    guess.append(userGuess)

    # Checks how many time the letter the user guessed appears in the solution and displays it
    count = solution.count(userGuess)
    print(userGuess, 'apperas', count, 'time(s) in the solution')

    # Updates the partial solution each time the user guesses correctly
    for i in range(len(solution)):
        if solution[i] == userGuess:
            partial_solution[i] = userGuess

    # Checks whether the user has guessed all the letters, if did, displays the comment
    if ''.join(partial_solution) == solution:
        print('You have guessed all!!!')
        break
    
