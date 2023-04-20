#The below code will run but is less human readable than ex17.py because I add read and write methods to the open function. It also assumes these methods close the files in python and is not a best practice. 

# Study Drills
# 1. This script is really annoying. #There’s no need to ask you before doing the copy, and it prints too much out to the screen.  #Try to make the script more friendly to use by removing features.
# 2. See how short you can make the script. I could make this one line long.
# 3. Notice at the end of the What You Should See section I used something called cat? It’s an old command that concatenates files together, but mostlyit’sjustaneasywaytoprintafiletothescreen.Typeman catto read about it.
# 4. Find out why you had to write out_file.close() in the code.       
# 5. Go read up on Python’s import statement, and start python3.6 to try it out. Try importing some things and see if you can get it right. It’s alright if you do not.

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file).read()

out_file = open(to_file,'w').write(in_file)

print("Alright, all done.")