# sets a variable named types of people equal to 10
types_of_people = 10 
# sets a variable containing a formated that passes through the variable types_of_people
x = f"There are {types_of_people} types of people."

#sets the variable binary equal to the string value binary
binary = "binary"
#sets the variable do_not equal to the value "don't"
do_not = "don't"
# set the variable y equal to a formatted sting that passes throuhg the varibales "binary" and "do_not"
y = f"Those who know {binary} and those who {do_not}."

#prints to terminal: "There are 10 types of people."
print(x)
#prints to terminal: "Those who know binary and those who don't."
print(y)

#prints to terminal: "I said: There are 10 types of people." by passing through the varible X.
print(f"I said: {x}")
#prints to terminal: "Those who know binary and those who don't." by passing through the varible y.
print(f"I also said: '{y}'")

#sets the variable hilarious equal to the boolean variable false. 
hilarious = False
#sets the variable joke_evaluation to "Isn't that joke so funny?!" and enables it to be modified by any future varibale using the {}s. 
joke_evaluation = "Isn't that joke so funny?! {}"

#prints the joke_evaluaiton string to terminal and modifies it using the format method with a passing in the value set in the hilarious variable.
print(joke_evaluation.format(hilarious))

#sets the variable w to the string below.
w = "This is the left side of..."
#sets the varibale e to the string below.
e = "a string with a right side."

#prints the variables w and e to terminal
print(w + e)