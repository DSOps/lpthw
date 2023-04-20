#imports the sys module, so paramters can be pased through to the script from the commmand line via 'argv'
from sys import argv
#sets the parameters "script" and "filename" to be provided an argument at script run
script, filename = argv
#create the variable "txt" and sets it equal to the function open(filename), which will open the ex15_sample.txt when it's provided as the argument at script run. 
txt = open(filename)
#prints the name of the file to the terminal
print(f"Here's your file {filename}:")
#prints the content of the variable "txt" ex15_sample.txt file using the read method
print(txt.read())
#prints the below string to the terminal
##print("Type the filename again:")
#sets the variable "file_again" equal to the input() function which will print ">" to the terminal when the variable is used in a later argument.
file_again =  input(">")
#set the variable "txt_again" to the open() function, which calls the input funciton in line 14
txt_again = open(file_again)
#prints ">" to the terminal, and then prints the content of a file given by a user to the terminal. 
#print(txt_again.read()) 