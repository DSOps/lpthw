#This is a varient to exercise 16, so that I can practice drills.

# Study Drills
# 1. If you do not understand this, go back through and use the comment trick to get it squared away in your mind. One simple English comment above each line will help you understand or at least let you know what you need to research more.
# 2. Write a script similar to the last exercise that uses read and argv to read the file you just created.
# 3. There’s too much repetition in this file. Use strings, formats, and escapes to print out line1, line2, and line3 with just one target.write() command instead of six.
# 4. Find out why we had to pass a 'w' as an extra parameter to open. Hint: open tries to be safe by making you explicitly say you want to write a file.
# 5. If you open the file with 'w' mode, then do you really need the target.truncate()? Read the documentation for Python’s open function and see if that’s true.

#imports the argv list from the sys module, so that parameters can be passed throuhg to the script
from sys import argv
#sets the paramaters "script" and "filename" to accept a parameter from argv at script execution
#filename = argv
script, filename = argv

#prints a formatted message to console that takes the "filename" parameter at script run and inpputs into the string. Tells the user how to cancel or allow the file deletion. CTRL-C will just terminate the script running at the input line. 
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")
#Prompts the user with an expectation of Return or CTRL-C
input("?")
#If Return is pressed, it continues the file and prints the next line.
print("Opening the file...")
#creates a variabe named "target" and sets it equal to the open function with parameter "filename" passed into it at the start of script run and writes to it, if it does not exist the file will be created. 
target =  open(filename,'w')

#prints the a message to the console the file is being truncated
print("Truncating the file. Goodbye!")
#truncates a file. When no paramter is listed, it truncates the file based at its current postion, which is set by the w mode for the open() function at 0 bytes in this case). This will cause anything in the file to be overwritten. If truncate() is given a size parameter, the truncate method will seek to the byte position provided and reduce the file size to that position. Any information after that file positio will be deleted.
target.truncate()

#prints the folliwng message to the console"
print("Now I'm going to ask you for three lines.")

#creates 3 variables, prompts the user to provide an input for each variable.
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

#prints the following message to the console
print("I'm going to write these to the file.")

#calls the target variable, which was defined as a file earlier and writes the varibles line1, line2, line 3 (which were provided by the user) and places a new line bewtween each variable written. 
target.write(line1 + "\n" + line2 + "\n" + line3 + "\n")

#prints a message to the console so the user knows the file is being closed.
print("And finally, we close it.")
#calls the target variable, which was defined as a file earlier and closes it.
target.close()