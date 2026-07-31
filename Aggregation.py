import pandas as pd

plants = pd.read_csv("data/plant_table.csv", sep=";")
average_by_species = plants.groupby("species_name")["leaf_count"].mean()
min_max = plants.groupby("species_name")["height_cm"].agg(["min", "max"])

print(average_by_species)
print(min_max)