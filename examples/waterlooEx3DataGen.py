import numpy as np

# Number of data points
n = 100000

m1 = np.random.uniform(0.1, 10, n)
m2 = np.random.uniform(0.1, 10, n)
r1 = np.random.uniform(0.1, 10, n)
r2 = np.random.uniform(0.1, 10, n)
gc = np.random.uniform(0.1, 10, n) # Gravitational constant

gPE = (gc * m1 * m2) * ((1/r1) - (1/r2))

pi1 = (r2 * gPE) / ((m1 * m1) * gc)
pi2 = m2/m1
pi3 = r1/r2

# Combine all variables into a single dataset
data = np.column_stack((m1, m2, r1, r2, gc, gPE))

# Save the original dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/WaterlooEx3.txt', data)

# Combine dimensionless quantities into a dataset
data_dimensionless = np.column_stack((pi2, pi3, pi1))

# Save the dimensionless dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/buckinghamWaterlooEx3.txt', data_dimensionless)
