""" Make a function that takes two arguments (given name and family name), the second of which is optional. 
Print a greeting according to which arguments are provided.
Example output: “Hello Kenneth.” or “Hello there, Kenneth of Lim!”  """

def greeting(forename, surname=False):
    if surname:
        print("Hello there, " + forename + " " + surname + "!")
    else:
        print("Hello " + forename + ".")

greeting("Alex", "Slocombe")
greeting("Alex")


""" Write a function that takes in any English word and turns it into pig latin. 
Extra if you can write another function that converts a whole sentence
Example input: “technique”, “omelet”, “string”
Example output: “echniquetay”, “omeletyay”, “ingstray” """

order = 0

def translate(word):
    for i in word:
        order += 1
    if order = 0:
        if i in "aeiou"
    else:
        return

translate("hello")

# I struggled a lot with this task
