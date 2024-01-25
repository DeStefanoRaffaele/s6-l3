import pandas as pd
import numpy as np
file_name = "./automobile.csv"
data = pd.read_csv(file_name)
#print(data.columns)
data_clean = pd.read_csv(file_name, usecols=list(range(9,14))+[16]+list(range(18,26))) #pulizia colonne dataset
#print(data_clean)
statistics = data_clean.describe() #calcolo statistico completo
print(statistics)
media = data_clean.mean(axis=0,numeric_only=True) #calcolo media per ogni colonna
print("Calcolo delle medie \n",media)
mediana = data_clean.median(axis=0,numeric_only=True) #calcolo mediana per ogni colonna
print("Calcolo delle mediane \n",mediana)

