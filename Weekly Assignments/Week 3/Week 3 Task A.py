""" Make a function that takes two arguments (given name and family name), the second of which is optional. 
Print a greeting according to which arguments are provided.
Example output: “Hello Kenneth.” or “Hello there, Kenneth of Lim!”  """

forename = str(input("Enter your first name: "))
surname = str(input("Enter your surname: "))

def greeting(forename, surname=False):
    if surname:
        print("Hello there, " + forename + " " + surname + "!")
    else:
        print("Hello " + forename + ".")

print(greeting(forename, surname))
