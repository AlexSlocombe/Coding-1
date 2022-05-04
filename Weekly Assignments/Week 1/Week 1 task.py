# Write a program that outputs “even” if a number is even and “odd” if a number is odd. 
# Think about what if the value is neither even nor odd 

while True:
    try:
        num = int(input("Enter an integer: "))
        if(num % 2) == 0:
            print("even")
        else:
            print("odd")
    except ValueError:
        print("That is not an integer, only integers can be either odd or even. Try again.")