## Yuria Loo
## IT 111: Project2
## 2024-04-12
## This program operates a file processing and lets a user
## add some texts to the file and copy it to a new file.


import os

# Opens a original file (Project2input.txt) for appending
originalFile = open('Project2Input.txt', 'a')

# Gets a user input for adding texts
getText = input('Enter a text to add ')
originalFile.write(getText)
originalFile.close()

# Opens the original file again
originalFile = open('Project2Input.txt')

# Opens the new file
newFile      = open('Project2Update.txt', 'w')

# Saves(creates) a copy of the file with a name of "Project2Update.txt"
for line in originalFile:
   newFile.write(line)

originalFile.close()
newFile.close()

# Deletes the original file
os.remove('Project2Input.txt')



