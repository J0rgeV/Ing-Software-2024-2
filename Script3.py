import matplotlib.pyplot as plt

def funcion(x):
    """
        Función que deseamos graficar.
    """
    return x ** 3

#Aquí mostramos la gráfica de la función.
x = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
y = []

for i in x:
    y.append(funcion(i))

plt.plot(x, y)
plt.show()