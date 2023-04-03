#Creates a variable that allows you to pass for literals into a string or print curly only the brackets.
formatter = "{} {} {} {}"

#prints the formatter string and uses the format method to insert the integers 1,2,3,4 into the formatter variable.
print(formatter.format(1, 2, 3, 4))
#prints the formatter string and uses the format method to insert the string one, two, three, four into the formatter variable.
print(formatter.format("one", "two", "three", "four"))
#prints the formatter string and uses the format method to insert the boolean True, False, False, True into the formatter variable.
print(formatter.format(True, False, False, True))
#prints the formatter string and uses the format method to insert the literals into the formatter variable.
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))