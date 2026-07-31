import pandas as pd
import matplotlib.pyplot as plt

plants =  pd.read_csv("data/plant_table.csv", sep=";")

#гістограма
plants["leaf_count"].plot(kind="hist", bins=5)
plt.title("Розподіл кількості листків")
plt.show()

#Точковий графік
plants.plot.scatter(x="height_cm", y="leaf_count")
plt.show()