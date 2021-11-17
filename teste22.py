def RemoveBrackets(strParam):
  output = 0 
  open_count = 0  #numero de parenteses aberto
  in_match = False #in match significa que achou e abriu um parenteses in_match fecha ou abre 
  #um parenteses
  for letra in strParam:
    if in_match:
      if letra == "(":
        open_count += 1
      else: 
        open_count -= 1
        if open_count == 0:
          in_match = False     
    else: 
      if letra == ")":
        output += 1
      else:
        in_match = True
        open_count += 1
  # code goes here
  return output + open_count

# keep this function call here 
print(RemoveBrackets(input()))