# Yuria Loo
# IT111: AD3 Search Files with RegGEx
# 2024-04-20

import re

# Lets a user to enter the name of the file
filename = input("Enter the file name (case sensitive): ")

# Lets a user to enter a search character
userTxt = input("Enter a search character expression: ")

# Checks the file for the search term line by line using RegEx
with open(filename) as f:
    print("File name: ", filename)
    for line in f:
        match = re.search("[" + userTxt + "]", line)
        if match:
            print(match.string)


