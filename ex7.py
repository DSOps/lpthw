#Prints below string to terminal
print("Mary had a little lamb.")
#Prints below string to terminal and {} with the .format method allows you to pass through a literal string.
print("Its fleece was white as {}.".format('snow'))
#Prints below string to terminal
print("and everywhere that Mary went.")
#Prints below string to terminal 10 times on the same line
print("." * 10) #what'd that do?

#Create a variable for each letter in the word cheeseburger  lines 11 through 22
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

#watch the comma at the end. try removing it and see what happens
#prints each letter of the word "Cheese" and end adds a space and appends the next print inline with the previous print.
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)