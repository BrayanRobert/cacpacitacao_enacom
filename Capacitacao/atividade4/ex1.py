import numpy as np
import matplotlib.pyplot as plt

# Definir a função objetivo e sua derivada
def f(x):
    return (x[0]-1)**2 + 2*x[1]**2 - 10

def df(x):
    return np.array([2*(x[0]-1), 4*x[1]])

# Plotar as curvas de nível da função objetivo
x1 = np.linspace(-10, 10, 100)
x2 = np.linspace(-10, 10, 100)
X1, X2 = np.meshgrid(x1, x2)
Z = f([X1, X2])
plt.contour(X1, X2, Z, levels=np.arange(-10, 50, 5))
plt.xlabel('x1')
plt.ylabel('x2')

# Implementar o algoritmo do gradiente
x = np.array([10, 10]) # ponto inicial
alpha = 0.1 # taxa de aprendizado
epsilon = 1e-2 # precisão
max_iter = 100 # número máximo de iterações
f_values = [f(x)] # valores de f ao longo das iterações
for i in range(max_iter):
    grad = df(x)
    if np.linalg.norm(grad) <= epsilon:
        break
    d = -grad / np.linalg.norm(grad)
    alpha = (d[0]*(x[0]-1) + 2*d[1]*x[1]) / (d[0]**2 + 2*d[1]**2)
    x = x + alpha * d
    f_values.append(f(x))

# Plotar o valor de f(x) ao longo das iterações
plt.figure()
plt.plot(f_values)
plt.xlabel('Número de iterações')
plt.ylabel('Valor de f(x)')

# Marcar o ponto ótimo x* no gráfico inicial
plt.plot(1, 0, marker='*', color='r', markersize=10)

plt.show()
