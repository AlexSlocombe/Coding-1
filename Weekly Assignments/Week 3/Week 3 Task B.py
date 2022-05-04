
""" Write a function that takes in any English word and turns it into pig latin. 
Extra if you can write another function that converts a whole sentence
Example input: “technique”, “omelet”, “string”
Example output: “echniquetay”, “omeletyay”, “ingstray” """

word = str(input("Enter a word: "))

if word[0] in {"a", "e", "i", "o", "u"}:
    word = word + "yay"
elif word[1] in {"a", "e", "i", "o", "u"}:
    word = word[1:len(word)] + word[0] + "ay"
else:
    word = word[2:len(word)] + word[0:1] + "lay"
print(word)
