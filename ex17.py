#imports the sys module with the argv command line list, allowing a user to pass in parameters from the command line.
from sys import argv
#imports the exists function that checks if a file already exists
from os.path import exists

#assigns 3 arguments provided through the command line to script, from_file, and to_file variables
script, from_file, to_file = argv

#prints formatted string to the console, displaying the source and destination file names provided by the user
print(f"Copying from {from_file} to {to_file}.")

#defines a variable using the open funciton "from_file" (the file being copied) in read mode (b/c its the default mode). This creates a file object that allows python to interact with file. 
in_file = open(from_file)
#defines a variable that contains the contents of a file [in this example it is a series of strings "yo yo yo3"]. Without the read method, a header would be retuned and not the contents of the file.
indata = in_file.read()

#prints a formatted message containing the number of bytes in the "indata" variable using len().
print(f"The input file is {len(indata)} bytes long")

#prints a formatted message that provides a boolean value using the exsits(). If a file with the name exists, the return will be True, else it will be False. 
print(f"Does the output file exist? {exists(to_file)}")
#prints the below string to the console."
print("Ready, hit RETURN to continue, CTRL-C to abort.")
#pauses the script and allows the user to contine the copy process or abort.
input()

#defines a varible containing a file object using the open() in write mode. The "to_file" is provided by the user via the command line.
out_file = open(to_file,'w')
#writes the contents of the "indata" variable to the "out_file" file object
out_file.write(indata)

#prints the message to the user stating the copy operation has been compelted.
print("Alright, all done.")

#closes the out_file to release system resources.
out_file.close()
#closes the in_file to release system resources.
in_file.close()