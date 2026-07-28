import numpy as np

heights = np.array([100, 50, 30, 10, 36])
leaf_counts = np.array([11, 6, 28, 49])

heights_m = heights / 100
new_leaf_counts = leaf_counts + 1

print(heights_m)
print(new_leaf_counts)