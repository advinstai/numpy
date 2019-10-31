import numpy as np

# Crie um array com 10 elementos usando a função arange
n = np.arange(1,11)
print(n)

# Transforme esse array de 1D (1x10) para 2D (2x5) usando a função reshape
n = n.reshape(2,5)
print(n)

# Crie duas matrizes bidimensionais com valores aleatórios
n = np.random.random((5,2))
m = np.random.random((3,4))
print("--- Matriz N (5x2):")
print(n)
print("--- Matriz M (3x4):")
print(m)

# calcule a transposta de cada matriz
n = np.transpose(n)
m = np.transpose(m)
print("--- Matriz N transposta (2x5):")
print(n)
print("--- Matriz M transposta (4x3):")
print(m)

# multiplique as duas matrizes
m1 = np.random.random((5,3))
m2 = np.random.random((3,4))
produto = np.dot(m1,m2)
print("--- Matriz resultado (5x4), contendo o produto m1(5x3)*m2(3x4):")
print(produto)

# Salve as matrizes de entrada e a de saída em arquivos. Qual o tamanho dos arquivos gerados?
''' Tamanho dos arquivos gerados:
m1.txt: 	375 bytes
m2.txt: 	300 bytes
produto.txt:	500 bytes
'''
np.savetxt("m1.txt",m1)
np.savetxt("m2.txt",m2)
np.savetxt("produto_m1_m2.txt",produto)


# Crie duas bidimensionais matrizes com valores aleatórios e gere uma única matriz 
# combinando linha a linha
arr1 = np.random.randint(0,11,(2,3))
arr2 = np.random.randint(0,11,(2,3))
print("--- Arr1:")
print(arr1)
print("--- Arr2:")
print(arr2)
arrConcat = np.concatenate((arr1,arr2),axis=0) # Concatena abaixo
print("--- arrConcat (axis=0):")
print(arrConcat)
arrConcat = np.concatenate((arr1,arr2),axis=1) # Concatena ao lado
print("--- arrConcat (axis=0):")
print(arrConcat)
arrConcat = np.concatenate((arr1,arr2),axis=None) # Concatena em vetor linha
print("--- arrConcat (axis=0):")
print(arrConcat)



