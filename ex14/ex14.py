from sys import argv

user_name, script = argv
prompt = '>'

print("Hi {}, I'm the {} script.".format(user_name, script))
print("I'd like to ask you a few questions.")
print("Do you like me {}?".format(user_name))
likes = input(prompt)

print("Where do you live {}?".format(user_name))
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("""
Alright, so you said {} about liking me.
you live in {}. Not sure where that is.
And you have a {} computer. Nice.
""".format(likes, lives, computer))
