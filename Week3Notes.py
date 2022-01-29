#Simple, basic function:

""" def add(a, b):
    print(a + b)

add(10, 8)

add(200, 477) """

# Advanced uses of functions

def greet(name):
    greetings = "Hello, " + name + "!"
    greetings += "Welcome to Coding One"
    return greetings

print(greet("Alex"))

def greet(name):
    greetings = "Hello, " + name + "!"

    def welcome(partial): 
        partial += " Welcome to Coding One"
        return partial

    greetings = welcome(greetings)

    return greetings

print(greet("Alex"))