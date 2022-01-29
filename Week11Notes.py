a = 1
b = 1

def fibonacci(a, b, iterations):
    for i in range(0, iterations):
        c= a + b
        a = b
        b = c
        print(c)

fibonacci(a, b, 5)
