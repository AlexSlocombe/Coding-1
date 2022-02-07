""" Make a program that uses a lookup table to convert any set of alphabets into 
their corresponding NATO phonetic alphabets. Also implement the inverse function. """

try:
    txt = str(input("Enter a word:"))
except ValueError as e:
    print("That was not a valid string")

NPA = {'a':'Alpha', 'b':'Bravo','c':'Charlie', 'd':'Delta', 'e':'Echo', 'f':'Foxtrot', 'g':'Golf', 'h': 'Hotel', 'i':'India', 'j':'Juliet', 'k':'Kilo', 'l':'Lima', 'm':'Mike', 'n':'November', 'o':'Oscar', 'p':'Papa', 'q':'Quebec', 'r':'Romeo', 's':'Sierra', 't':'Tango', 'u':'Uniform', 'v':'Victor', 'w':'Whiskey', 'x':'Xray', 'y':'Yankee', 'z':'Zulu'}

for i in txt:
    print(NPA[i])

# To convert NATO back into letters

nato = (input(str("Enter NATO phonetic alphabet: ")))
set_n = nato.split()

for i in set_n:
    for alpha, beta in NPA.items():
        if i in beta:
            print(alpha, end = " ")



""" Implement a Caesar Cipher function that takes a string and shift 
amount, outputs the encrypted string. """

# I could not complete this

""" try:
    txt = str(input("Enter some text: "))
    shift = int(input("Enter the decryption shift: "))
except ValueError as e:
    print("That was not a valid entry. Enter a string for text or an integer for the decryption shift.")

for i in txt:
    if i == " ":
        break
    else: """

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

