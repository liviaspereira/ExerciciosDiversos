def calcular_palavra(palavra):
    if len(palavra) <= 10:
        return "Tente uma palavra maior"
    elif len(palavra) >= 11 and len(palavra) <= 20:
        return "Boa Palavra"
    else:
        return "Uau!"


palavra1 = calcular_palavra("jurandir"))

print(palavra1)






