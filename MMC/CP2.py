import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 100)

# Parábola
y_parabola = x**2

# Retas
y_ab = x + 2
y_ac = 2*x

# Pontos
A = (2, 4)
B = (-1, 1)
C = (0, 0)

plt.plot(x, y_parabola, label='y = x²')
plt.plot(x, y_ab, '--', label='Reta AB: y = x + 2')
plt.plot(x, y_ac, '--', label='Reta AC: y = 2x')

plt.scatter(*A)
plt.scatter(*B)
plt.scatter(*C)

plt.text(2,4,' A')
plt.text(-1,1,' B')
plt.text(0,0,' C')

plt.axhline(0)
plt.axvline(0)

plt.legend()
plt.grid()
plt.title('Parábola e Retas')

plt.show()