# Questão 4

import numpy as np
import matplotlib.pyplot as plt

def G(x):
    if x < 0:
        return -x - (x - 3) - (2 * x - 7) - (x - 9)
    elif 0 <= x < 3:
        return x - (x - 3) - (2 * x - 7) - (x - 9)
    elif 3 <= x < 3.5:
        return x + (x - 3) - (2 * x - 7) - (x - 9)
    elif 3.5 <= x < 9:
        return x + (x - 3) + (2 * x - 7) - (x - 9)
    else:  # x >= 9
        return x + (x - 3) + (2 * x - 7) + (x - 9)

# Gerando pontos para o gráfico
x_values = np.linspace(-10, 10, 400)
y_values = [G(x) for x in x_values]

# Configurando o gráfico
plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='G(x)')
plt.title('Gráfico da Função G(x)')
plt.xlabel('x')
plt.ylabel('G(x)')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.show()

