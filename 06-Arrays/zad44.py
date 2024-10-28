import matplotlib.pyplot as plt

x = []
y = []


for n in range(-100, 101):
    x.append(n)

for n in x:
    y.append(n ** 2 - 3)


plt.plot(x, y, label='f(x) = x^2 - 3', color='blue')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Graph of f(x) = x^2 - 3')
plt.show()
