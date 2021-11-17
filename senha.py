"""
In this Kata you will need to write a function that returns whether a password is strong or not.

Your code should return a Boolean of true if the provided password meets the following conditions

    password must be no less than 8 characters long
    password must have at least 1 capital letter
    password must have at least 1 number
    password must have at least 1 special character

for this Kata special characters are considered ( ! " # $ % & ' ( ) * + ' - . / ; : < > = or ?)

if the password doesn't meet these requirements return false.

>>> tem_mais_de_8_char("batata")
False

>>> tem_mais_de_8_char("1234567")
False

>>> tem_mais_de_8_char("123456123456")
True

>>> pelo_menos_1_char_maiusculo("abc")
False

>>> pelo_menos_1_char_maiusculo("ABC")
True

>>> pelo_menos_1_numero("123")
True

>>> pelo_menos_1_numero("abc")
False

>>> pelo_menos_1_char_especial("!asd")
True

>>> pelo_menos_1_char_especial("asdfg")
False

>>> verifica_senha("A123abc1235!!")
True

>>> verifica_senha("123")
False
"""

def tem_mais_de_8_char(senha):
    return len(senha) >= 8

def pelo_menos_1_char_maiusculo(senha):
    for letra in senha:
        if letra.isupper():
            return True
    return False

def pelo_menos_1_numero(senha):
    for letra in senha:
        if letra.isnumeric():
            return True
    return False

def pelo_menos_1_char_especial(senha):
    chars = "!\"#$%&'()*+'-./;:<>=?"
    for letra in senha:
        if letra in chars:
            return True
    return False

def verifica_senha(senha):
    return all(
        [
            tem_mais_de_8_char(senha),
            pelo_menos_1_char_maiusculo(senha),
            pelo_menos_1_numero(senha),
            pelo_menos_1_char_especial(senha)
        ]
    )