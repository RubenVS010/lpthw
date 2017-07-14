#This one is like your script with argv
def print_two(*args):
    arg1, arg2 = args
    print("arg1:{}, arg2:{}".format(arg1, arg2))

#ok, that *args is actually pointless since you can do this
def print_two_again(arg1, arg2):
    print("arg1:{}, arg2:{}".format(arg1, arg2))

#This takes just one argument.
def print_one(arg1):
    print("I got nothing.")

#This takes no arguments
def print_none():
    print("I got nothing")

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()


