import numpy as np
import matplotlib.pyplot as plt

# Define the range for n (approximate -infinity to 0)
n = np.arange(-5, 1) # Array from -100 to 0

# Calculate y(n) = (1/3)^(-n)
y = (1/3)**(-n)

# Calculate the sum
numerical_sum = np.sum(y)

print(f"Theoretical Sum: 3/2 = {3/2:.5f}")
print(f"Numerical Sum (first 100 terms): {numerical_sum:.5f}")

# Visualization of the sequence y(n)
plt.figure(figsize=(8, 4))
plt.stem(n[-15:], y[-15:], basefmt=" ") # Plot only the last 15 terms for clarity
plt.title('Sequence y(n) approaching 0')
plt.xlabel('n')
plt.ylabel('y(n)')
plt.grid(True)
plt.show()
