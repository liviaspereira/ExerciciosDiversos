'''Guarde na variável media_contas o valor da média da colula total'''
import pandas as pd

gorjeta = pd.read_csv("gorjeta.csv").to_dict()

df = pd.DataFrame(gorjeta)
min_gorjeta = df['gorjeta'].min()
print(min_gorjeta)



