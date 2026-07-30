import pandas as pd

plants = pd.read_csv("data/plant_table.csv", sep="\t")
leaves_count = plants[plants["leaf_count"]>10]

red_or_tall = plants[
    (plants["height_cm"]>50)|
    (plants["color"]=="red")
]

print(leaves_count)
print(red_or_tall)