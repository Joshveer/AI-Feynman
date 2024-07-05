import numpy as np

# Number of data points
n = 100000

g = np.random.uniform(1, 10, n)
m1 = np.random.uniform(1, 10, n)
m2 = np.random.uniform(1, 10, n)
r = np.random.uniform(1, 10, n)

f = (-g * m1 * m2) / (r * r)

pi1 = (f * r * r) / (m1 * m2 * g)
pi2 = m2/m1

# Combine all variables into a single dataset
data = np.column_stack((g, m1, m2, r, f))

# Save the original dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/WaterlooEx6.txt', data)

# Combine dimensionless quantities into a dataset
data_dimensionless = np.column_stack((pi2, pi1))

# Save the dimensionless dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/buckinghamWaterlooEx6.txt', data_dimensionless)
