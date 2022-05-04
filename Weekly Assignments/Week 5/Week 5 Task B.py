""" Implement a Caesar Cipher function that takes a string and shift 
amount, outputs the encrypted string. """

try:
    txt = str(input("Enter some text: "))
    shift = int(input("Enter the decryption shift: "))
except ValueError:
    print("That was not a valid entry. Enter a string for text or an integer for the decryption shift.")

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in txt:
    reorder = alphabet.index(i) + shift
    if i == ' ':
        pass
    else:
        print(alphabet[reorder])
