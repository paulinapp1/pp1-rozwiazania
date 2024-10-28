import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x / (np.log(x) ** 2)

x_values = np.linspace(0.01, 5, 100) 


y_values = f(x_values)

# Plot the function
plt.plot(x_values, y_values, label=r'$\frac{x}{(\ln x)^2}$', color='pink')
plt.title('Plot of $f(x) = \\frac{x}{(\\ln x)^2}$')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()
