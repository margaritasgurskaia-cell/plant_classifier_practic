import pandas as pd

plants = pd.read_csv("data/plant_table.csv", sep=";")

print(plants.columns)
print(plants.head())

by_color = plants.groupby("color")
by_species = plants.groupby("species_name")

print(by_color)
print(by_species)