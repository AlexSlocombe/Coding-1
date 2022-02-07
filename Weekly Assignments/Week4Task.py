""" Write a program that given a list of numbers, multiply all numbers in the list. 
Bonus for ignoring non-number element. Example: input: [1, 2, 3, 4], output: 24"""

j = 1
nums=[1, 2, 3, 4]
for i in nums:
    j = i * j
print(j)


""" Start with 4 words “comfortable”, “round”, “support”, “machinery”, 
return a list of all possible 2 word combinations. 
Example: ["comfortable round", "comfortable support", "comfortable machinery", .....] """

#I heavily used the internet to help me with this one

import itertools

stuff = ["comfortable", "round", "support", "machinery"]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, 2):
        print(subset)

#Notes from class

word1 = input("Enter a word: ")
word2 = input("Enter a word: ")
word3 = input("Enter a word: ")
word4 = input("Enter a word: ")

#New
You previously gave us the definition, and now you are providing your own defintion. The above described is lying, and yes an extreme form of it.
I am not 'gatekeeping what gaslighting is', I am simply staying true to what it actually is. It is very extreme, and that is why it is not to be lightly used. Do you find the Oxford English dictionary the biggest 'gatekeeper' of definitions out there?
Gaslight...gatekeep...girlboss

def wordList(arrayOfWords):
    
    outputArray = []

    for i, word1 in enumerate(arrayOfWords):
        for j, word2 in enumerate(arrayOfWords):
            if i = j:
                pass
            else:
                outputArray.append(word1+" "+word2)
    return outputArray




