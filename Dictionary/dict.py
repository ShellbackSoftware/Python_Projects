# Reads in a JSON of a dictionary and allows the user to look up words, with recommendations 
# if the word is spelled wrong
import json
from difflib import get_close_matches

# Data is a (literal) dictionary where the keys are the words, and values are the definitions
data = json.load(open("Dictionary/data.json"))

def lookUp(word):
    if word in data: # Word is correctly in spelled
        return (data[word])
    elif word.title() in data: # Checks for proper nouns
        return data[word.title()]
    elif word.upper() in data: # Checks for acronyms
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys())) > 0: # Spelled the word wrong, get something similar
        valid = False
        while not valid:
            yn = input ("'{}' does not exist. Did you mean '{}' ? (Y/N): ".format(word, get_close_matches(word,data.keys())[0])).strip().lower()
            if yn == "y" or yn == "yes":
                return data[get_close_matches(word, data.keys())[0]]
            elif yn == "n" or yn == "no":
                print("Okay. Spell better next time!")
                valid = True
            else:
                print("Please enter 'Y', 'Yes', 'N', or 'No'.")
                continue                
    else:
        return "That string of letters doesn't exist. Are you sure you spelled a word?"

word = input("Please enter a word to look up: ").strip().lower()

output = lookUp(word)
if type(output) == list: # In case there are multiple definitions
    for defs in output:
        print(defs)
else:
    print(output)