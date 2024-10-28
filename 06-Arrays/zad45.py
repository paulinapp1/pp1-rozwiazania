import matplotlib.pyplot as plt
import math

x = []
y = []


for angle in range(361):
    x.append(math.radians(angle)) 

for angle_rad in x:
    y.append(math.sin(angle_rad))

# display chart
plt.plot(x, y, label='y = sin(x)', color='pink')
plt.xlabel('Angle (radians)')
plt.ylabel('sin(x)')
plt.title('Graph of y = sin(x) for 0-360 degrees')

plt.show()
