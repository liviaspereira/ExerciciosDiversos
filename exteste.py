'''Camel Case
Have the function CamelCase(str) take the str parameter being passed and return it in 
proper camel case format where the first letter of each word is capitalized (excluding 
the first letter). The string will only contain letters and some combination of 
delimiter punctuation characters separating each word.

For example: if str is "BOB loves-coding" then your program should return the 
string bobLovesCoding.
Examples
Input: "cats AND*Dogs-are Awesome"
Output: catsAndDogsAreAwesome
Input: "a b c d-e-f%g"
Output: aBCDEFG '''

import string
def CamelCase(strParam):
  valid_characters = string.ascii_letters
  output = ""
  in_word = False #saber se está dentro de uma palavra
  for letra in strParam:
    if in_word:
      if letra in valid_characters:
         output += letra.lower()
      else:
        in_word = False

    else:
      if letra in valid_characters:
        in_word = True
        if output == "":
          output += letra.lower()
        else: 
          output += letra.upper()


  # code goes here
  return output

# keep this function call here 
print(CamelCase(input()))