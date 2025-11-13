import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 + 2*x + 3
x = np.linspace(-10, 10, 400)  # 400 points from -10 to 10
y = f(x)
plt.plot(x, y, label='f(x) = x^2 + 2x + 3', color='blue')
plt.title('Plot of f(x) = x^2 + 2x + 3')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.legend()
plt.show()
