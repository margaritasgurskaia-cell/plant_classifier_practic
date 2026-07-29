import pandas as pd

plants = pd.DataFrame({
    "name": ["catalpa", "lavender", "willow"],
    "leaf_count": [10000, 500, 100000],
    "color": ["green","violet", "pale green"]
})

print(plants.head())

leaf_table = plants[["name", "leaf_count"]]

print(leaf_table)