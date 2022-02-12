'''Write a function that takes in a string of one or more words, and returns the same string, but 
with all five or more letter words reversed (Just like the name of this Kata). Strings passed 
in will consist of only letters and spaces. Spaces will be included only when more than one word
 is present.
'''

def inverter_string(string):
    string_separaras = string.split()
    if len(string_separaras) > 5:
        return inverter_string[::-1]
    else: 
        return string

print(inverter_string("Caralho dos Infernos"))




