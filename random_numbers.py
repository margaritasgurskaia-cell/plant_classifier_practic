#перший варіант

import numpy as np

leaf_counts = np.random.randint(3, 16, size=10)
averange_leaf_counts = sum(leaf_counts)/len(leaf_counts)

print(leaf_counts)
print(averange_leaf_counts)

#другий варіант

leaf_counts = np.random.randint(3, 16, size=10)

print(leaf_counts)
print(leaf_counts.mean())