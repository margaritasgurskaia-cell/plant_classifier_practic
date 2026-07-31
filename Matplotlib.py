import pandas as pd
import matplotlib.pyplot as plt

plants = pd.read_csv("data/plant_table.csv", sep=";")

plt.plot(plants["leaf_count"])
plt.title("Кількість листків рослин")
plt.xlabel("Номер вимірювання")
plt.ylabel("Кількість, шт.")
plt.show()