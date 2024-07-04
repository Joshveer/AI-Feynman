import numpy as np

# Number of data points
n = 100000

f = np.random.uniform(1, 10, n)
d = np.random.uniform(1, 10, n)
l = np.random.uniform(1, 10, n)
p = np.random.uniform(1, 10, n)
v = np.random.uniform(1, 10, n)

pf = f * (l/d) * ((p * v * v)/2)

pi1 = pf/((p * v * v))
pi2 = l/d
pi3 = f

# Combine all variables into a single dataset
data = np.column_stack((f, d, l, p, v, pf))

# Save the original dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/WaterlooEx4.txt', data)

# Combine dimensionless quantities into a dataset
data_dimensionless = np.column_stack((pi2, pi3, pi1))

# Save the dimensionless dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/buckinghamWaterlooEx4.txt', data_dimensionless)
