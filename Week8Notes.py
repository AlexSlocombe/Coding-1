import sys

#command line arguments

#allow user to sum numbers in command line
print(sys.argv[1: ])

def sum_numbers(nums):
    return sum(nums)

numbers_to_sum = [int(i) for i in sys.argv[1:]] #list comprehension to convert integers to numbers
print(sum_numbers(numbers_to_sum))


#Reading and writing files

file = open("example.txt")
print(file.read()) #allows you to open and read a txt file
file.close()

with open("example.txt") as file:
    print(file.read()) #removes the need for file.close

with open("example.txt") as file:
    print(file.write("She done already had herses\n"))#\n ends the line
    file.writeline("I'm like hey whatsup hello")
    file.writelines(["34\n","53\n","68\n"])


# Using and parsing command line flags
