#variable that has the value of an string that indents when printed due to the \t escape sequenece
tabby_cat =  "\tI'm tabbed in."
#variable that has the value of an string that creates a new line when printed due to the \n escape sequenece
persian_cat = "I'm split\non a line."
#variable that has the value of an string that has a backslash string in it  when printed due to the \\ escape sequenece
backslash_cat = "Im \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food 
\t* Fishes
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)