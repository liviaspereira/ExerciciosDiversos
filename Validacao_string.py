import re 

def CodelandUsernameValidation(strParam):

  if len(strParam) <= 25 and len(strParam) >= 4:
    if strParam[0].islower():  
      pattern = "^[A-Za-z0-9_]*$"
      if bool(re.match(pattern, strParam)):
        if strParam[-1] != "_":
          return True
        else:
          return False
      else: 
        return False
    else:
      return False
  else:
      return False
    

# keep this function call here 
print(CodelandUsernameValidation(input()))
