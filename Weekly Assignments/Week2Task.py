""" Given 3 positive integers, find the sum of all numbers between the first two that are a 
multiple of the third. eg. Given "1, 10, 2", the expected output is "20". """

""" a = 1
b = 10
c = 2
d = 0

for i in range(a, b):
    if(i % c)==0:
        d = d + i

print(d) """



""" Given a string of text, print the number of times each letter in the alphabets a-z appear. 
Hint: “a” != “A”. eg. Given "the quick brown fox jumps over the lazy dog", 
the expected output is "a: 1, b: 1, c: 1, d: 1, e: 3 ......" """

# I struggled with this question, and couldn't find a solution
    
input = "the quick brown fox jumps over the lazy dog"
alphabet = "abcdefghijklmnopqrstuvwxyz"

for i in alphabet:
    count = 0
    for j in input:
        if i == j:
            count = count + 1

print(i + ": " + str(count))



""" Implement division as a series of subtraction. 
The program should only deal with integers and report the remainder if there is one. 
eg. 10/2 => 10-2-2-2-2-2=0, 10 minus 2 five times so the division result is 5 with a remainder of 0 """

""" a = 10
b = 2
index = 0

while a - b >= 0:
    a = a - b
    index += 1

print(index, "remainder", a) """