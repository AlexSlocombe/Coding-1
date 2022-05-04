""" Start with 4 words “comfortable”, “round”, “support”, “machinery”, 
return a list of all possible 2 word combinations. 
Example: ["comfortable round", "comfortable support", "comfortable machinery", .....] """

import itertools

stuff = ["comfortable", "round", "support", "machinery"]
for L in range(0, len(stuff)+1):
    for subset in itertools.combinations(stuff, 2):
        print(subset)