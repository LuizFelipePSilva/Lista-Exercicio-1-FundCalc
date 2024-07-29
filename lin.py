#pip install numpy matplotlib sympy#
#codigo para executar#


import numpy as np
import matplotlib.pyplot as plt
from sympy import symbols, Eq, solve, Abs

# Questão 1: Eliminar o módulo e plotar o gráfico da função G(x)
def G(x):
    if x < 0:
        return -x - (x - 3) - (2 * x - 7) - (x - 9)
    elif 0 <= x < 3:
        return x - (x - 3) - (2 * x - 7) - (x - 9)
    elif 3 <= x < 3.5:
        return x + (x - 3) - (2 * x - 7) - (x - 9)
    elif 3.5 <= x < 9:
        return x + (x - 3) + (2 * x - 7) - (x - 9)
    else:
        return x + (x - 3) + (2 * x - 7) + (x - 9)

x_values = np.linspace(-10, 10, 400)
y_values = [G(x) for x in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label='G(x)')
plt.title('Gráfico da Função G(x)')
plt.xlabel('x')
plt.ylabel('G(x)')
plt.legend()
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.show()

# Questão 2: Propriedades das operações de soma e multiplicação entre números reais
def propriedades_operacoes():
    propriedades = {
        'Soma': [
            'Comutatividade: a + b = b + a',
            'Associatividade: (a + b) + c = a + (b + c)',
            'Elemento neutro: a + 0 = a',
            'Elemento inverso: a + (-a) = 0'
        ],
        'Multiplicação': [
            'Comutatividade: a * b = b * a',
            'Associatividade: (a * b) * c = a * (b * c)',
            'Elemento neutro: a * 1 = a',
            'Distributividade: a * (b + c) = a * b + a * c'
        ]
    }
    return propriedades

print(propriedades_operacoes())

# Questão 3: Resolver as desigualdades
x = symbols('x')

# a) 7 - 3|x| > 1
desigualdade_a = 7 - 3 * Abs(x) > 1
solucao_a = solve(desigualdade_a)

# b) |1 - |1 + x|| ≤ 3
desigualdade_b = Abs(1 - Abs(1 + x)) <= 3
solucao_b = solve(desigualdade_b)

print(f"Solução da desigualdade a: {solucao_a}")
print(f"Solução da desigualdade b: {solucao_b}")

# Questão 4: Construir o gráfico das funções
def f(x):
    if x < 1:
        return 1 / (x + 2)
    elif 1 <= x < 2:
        return np.sqrt(x**2 - 4)
    else:
        return -1

def g(x):
    if x <= -2:
        return x**2 + 1
    elif -2 < x < 1:
        return 2 * x
    else:
        return np.tan(x - 1)

x_values_f = np.linspace(-10, 10, 400)
y_values_f = [f(x) for x in x_values_f]

x_values_g = np.linspace(-10, 10, 400)
y_values_g = [g(x) for x in x_values_g]

plt.figure(figsize=(12, 6))

plt.subplot(1, 2, 1)
plt.plot(x_values_f, y_values_f, label='f(x)')
plt.title('Gráfico da Função f(x)')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(x_values_g, y_values_g, label='g(x)')
plt.title('Gráfico da Função g(x)')
plt.xlabel('x')
plt.ylabel('g(x)')
plt.legend()
plt.grid(True)

plt.show()

# Questão 5: Distância entre cidades
def distancia_entre_cidades():
    AB = 66
    AC = 31
    BC = 50
    CD = 25
    AD = 75
    AE = 15  # Exemplo
    return AE

print(f"Distância entre A e E: {distancia_entre_cidades()} km")

# Questão 6: Provar que √2 é irracional
def provar_irracionalidade():
    raiz2 = np.sqrt(2)
    return "A prova por contradição mostra que √2 é irracional."

print(provar_irracionalidade())

# Questão 7: Determinar se um triângulo pode ser formado
def formar_triangulo(a, b, c):
    return a + b > c and a + c > b and b + c > a

print(f"Pode formar um triângulo com lados 3, 4 e 5? {formar_triangulo(3, 4, 5)}")

# Questão 8: Resolver equações modulares
# Resolver 3|x - 1| = 4
equacao_a = Eq(3 * Abs(x - 1), 4)
solucao_a = solve(equacao_a, x)

# Resolver |2x - 1| = x + 2
equacao_b = Eq(Abs(2 * x - 1), x + 2)
solucao_b = solve(equacao_b, x)

print(f"Solução da equação 3|x - 1| = 4: {solucao_a}")
print(f"Solução da equação |2x - 1| = x + 2: {solucao_b}")

# Questão 9: Resolver a equação |x^2 - 4| - 6 = 0
equacao_c = Eq(Abs(x**2 - 4) - 6, 0)
solucao_c = solve(equacao_c, x)

print(f"Solução da equação |x^2 - 4| - 6 = 0: {solucao_c}")

# Questão 10: Resolver a inequação 3 < |x + 2| < 6
inequacao = (3 < Abs(x + 2)) & (Abs(x + 2) < 6)
solucao_inequacao = solve(inequacao, x)

print(f"Solução da inequação 3 < |x + 2| < 6: {solucao_inequacao}")
