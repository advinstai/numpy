# Crie um vetor nulo de tamanho 10

import numpy as np

array = np.empty(10)


# Como encontrar o tamanho da memória de qualquer matriz

print(array.size * array.itemsize)

# Crie um vetor nulo de tamanho 10, mas o quinto valor, que é 1

array[4] = 1

# Crie um vetor com valores que variam de 10 a 49

array = np.random.randint(10, 50, size=10)
print(array)

# Inverter um vetor (o primeiro elemento se torna o último)

array = array[::-1]
print(array)


# Crie uma matriz 3x3 com valores que variam de 0 a 8

array = np.random.randint(0, 9, size=(3, 3))
print(array)

# Crie uma matriz de identidade 3x3

array = np.eye(3)
print(array)

# Crie uma matriz 3x3x3 com valores aleatórios

array = np.random.random(size=(3, 3, 3))
print(array)

# Crie uma matriz 10x10 com valores aleatórios e encontre os valores mínimo e máximo

array = np.random.random(size=(10, 10))
print(array, 'max', array.max(), 'min', array.min())

# Crie um vetor aleatório de tamanho 30 e encontre o valor médio

array = np.random.random(size=(30))
print(array, 'mean', array.mean())

# Crie uma matriz 2D com 1 na borda e 0 dentro

array = np.zeros((10, 10))
array[0, :] = 1
array[-1, :] = 1
array[:, 0] = 1
array[:, -1] = 1
print(array)


# Crie uma matriz 5x5 com valores 1,2,3,4 logo abaixo da diagonal

array = np.eye(5)
for i in range(4):
    array[i + 1, i] = i + 1
print(array)


# Crie uma matriz estruturada representando uma posição (x, y) e uma cor (r, g, b)

array = np.random.randint(0, 256, size=(8, 10, 3))
print(array)

# Subtrair a média de cada linha de uma matriz

mean = array.mean(axis=1)
mean = np.expand_dims(mean, axis=1)
print(array - mean)


# Como encontrar o valor mais frequente em uma matriz?

from scipy import stats
print(stats.mode(array.flatten()))

# Crie uma matriz a partir de um arquivo
array = np.load('matriz.npy')
print(array)

# crie uma matriz com valores aletaórios e salve para um arquivo

array = np.random.randint(0, 256, size=(8, 10, 3))
np.save('matriz', array)
print(array)


