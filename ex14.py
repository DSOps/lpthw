from sys import argv

script, user_name, whatever = argv
prompt = 'C\'mon answer>>'

print(f"Hi {user_name}, I'm the script {script}.")
print("I'd like to ask you a few questons.")
print(f"Do you like me {user_name}?")
likes = input(prompt)

print(f"Where do you live {user_name}?")
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print(f"""
Alright, so you said {likes} about liking me.
you live in {lives}. Not sure where that is.
And you have a {computer} computer. Nice.""")

#My study drill addition line 3 has a related argv
print(input(whatever))