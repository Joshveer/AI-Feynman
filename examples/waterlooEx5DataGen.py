import numpy as np

# Number of data points
p = 100000

n0 = np.random.uniform(1, 10, p)
m = np.random.uniform(1, 10, p)
g = np.random.uniform(1, 10, p)
x = np.random.uniform(1, 10, p)
kb = np.random.uniform(1, 10, p)
temp = np.random.uniform(1, 10, p)

n = n0 * (2.71828 ** ((-(m * g * x))/((kb * temp))))

pi1 = (kb * temp) / (m * g * x)
pi2 = n
pi3 = n0

# Combine all variables into a single dataset
data = np.column_stack((n0, m, g, x, kb, temp, n))

# Save the original dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/WaterlooEx5.txt', data)

# Combine dimensionless quantities into a dataset
data_dimensionless = np.column_stack((pi1, pi3, pi2))

# Save the dimensionless dataset to a text file
np.savetxt('/Volumes/T7/Waterloo/AI-Feynman/example_data/buckinghamWaterlooEx5.txt', data_dimensionless)
