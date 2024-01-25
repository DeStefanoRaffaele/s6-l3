import pandas as pd
file_data = "./iris_data.csv"
data = pd.read_csv(file_data)
#print(data)
print("Stampiamo le prime 5 righe: \n",data.head(5))
print("Stampiamo i nomi delle colonne: \n", data.columns)
#importa 7. Attribute Information:  1. sepal length in cm 2. sepal width in cm 3. petal length in cm 4. petal width in cm 5. class dal file iris_nome.csv
data_modif = pd.read_csv(file_data, names=["sepal length","sepal width","petal length","petal width","class"])

print("Stampiamo le prime 5 righe: \n",data_modif.head(5))
print("Stampiamo le ultime 10 righe:\n",data_modif.tail(10))

#Stampiamo un riepilogo dei descrittori statistici del dataset
statitics = data_modif.describe(exclude="object")
print(statitics)