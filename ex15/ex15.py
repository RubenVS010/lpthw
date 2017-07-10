#Import argv from the sys module.
from sys import argv

#This create some nice variables for argv, keep in mind to also use these when
#Calling the script, if you do not use the arguments it will not be executed
#Untill you specify all the arguments.
script, filename = argv

#Specify var for filename   
txt = open(filename)

#Print string + read file and print it on screen.
print("Here's your file %r:" % filename)
print(txt.read())

#Again ask the user for the filename, and print it on the screen. 
print("Type the filename again:")
file_again = input("~>")

txt_again = open(file_again)
#refer to line 16.
print(txt_again.read())
