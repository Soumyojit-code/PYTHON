import numpy as np
import matplotlib.pyplot as plt

# Define the function
def f(x):
    return x**2 + 2*x + 3

# Generate x values
x = np.linspace(-10, 10, 400)  # 400 points from -10 to 10

# Calculate y values
y = f(x)

# Create the plot
plt.plot(x, y, label='f(x) = x^2 + 2x + 3', color='blue')
plt.title('Plot of f(x) = x^2 + 2x + 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()

# Show the plot
plt.show()
