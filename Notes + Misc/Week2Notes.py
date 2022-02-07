# While loop
""" a = 2
b = 2
c = 0

while c < 100:
    c = c + a
    b = a * c

    if b > 200:
        break (Ends loop before full run)
print(c)  """ #shift + alt + A commented this whole section out

#For loop
""" a = 2
b = 2
c = 0

for i in range(0, 50): #runs the function 50 times
    c = c+ a
print(c)  """# prints 100

#Fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# a, b, a+b
# _, a, b,

a = 0
b = 1

number_iterations = 10
index = 0

print(a)
print(b)
while index < number_iterations:
    print(a + b)
    c = a + b

    a = b
    b = c 

    index += 1
