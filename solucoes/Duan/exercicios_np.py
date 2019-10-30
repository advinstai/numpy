import numpy as np

# Crie um vetor nulo de tamanho 10
n = np.zeros(10,dtype=np.int16)
print(n)
print("---")

# Como encontrar o tamanho da memória de qualquer matriz
'''
np.size: retorna o numero de elementos do array
np.itemsize: retorna o espaco que 1 elemento do array ocupa na memoria
---> multiplicando os dois sabe-se o tamanho que o array inteiro ocupa na memoria
'''
print("Size:",n.size)
print("Item size:",n.itemsize)
print("Espaco ocupado na memoria:",n.nbytes,"bytes.")
print("---")

# Crie um vetor nulo de tamanho 10, mas o quinto valor, que é 1
n = np.zeros(10,dtype=np.int16)
n[4] = 1
print(n)
print("---")
# Crie um vetor com valores que variam de 10 a 49
n = np.random.randint(10,49+1,(3,3))
print(n)
print("---")

# Inverter um vetor (o primeiro elemento se torna o último)
'''A funcao np.flip() inverte a ordem dos elementos no vetor, mantendo sua ordem'''
n = np.flip(n)
print(n)
print("---")

# Crie uma matriz 3x3 com valores que variam de 0 a 8
n = np.random.randint(0,9,(3,3))
print(n)
print("---")

# Crie uma matriz de identidade 3x3
'''Lembrete: "dtype=np.int16" serve pra transformar em integer'''
n = np.eye(3,dtype=np.int16)
print(n)
print("---")

# Crie uma matriz 3x3x3 com valores aleatórios
n = np.random.randint(0,10,(3,3,3))
print(n)
print("---")

# Crie uma matriz 10x10 com valores aleatórios e encontre os valores mínimo e máximo
n = np.random.randint(0,100,(10,10))
nMin = np.ndarray.min(n)
nMax = np.ndarray.max(n)
print("Min in n:",nMin)
print("Max in n:",nMax)
print("---")

# Crie um vetor aleatório de tamanho 30 e encontre o valor médio
n = np.random.randint(0,100,(30))
nMin = np.ndarray.min(n)
nMax = np.ndarray.max(n)
print("Valor medio:",round((nMax-nMin)/np.size(n),2))
print("---")

# Crie uma matriz 2D com 1 na borda e 0 dentro
m = np.zeros((3,3))
''' Formato np.pad():
(array, tamanho da borda, modo ('constant'),constant_values=()) '''
m = np.pad(m,(1),'constant',constant_values=(1))
print(m)
print("---")

# Crie uma matriz 5x5 com valores 1,2,3,4 logo abaixo da diagonal

'''--- OPCAO 1:'''
''' Formato np.diag():
(array, k), onde k eh a posicao da diagonal (defaul: 0)
---> Como a questao pede "logo abaixo da diagonal", k=-1

---> O output sera uma array de zeros com diagonal(-1) igual a 1,2,3,4
'''
n = np.diag(1+np.arange(4),k=-1)
print(n)
print("---")

'''--- OPCAO 2:'''
n = np.random.randint(1,5,(5,5))
''' Formato np.tril():
(array,k), onde k indica o deslocamento da diagonal principal
    ao qual sera levado em conta para zerar os elementos acima de k.
Ex: k=0: zera elementos acima da diagonal principal
    k=1: zera elementos acima da diagonal principal+1
    k=-1: zera elementos acima da diagonal principal-1
'''
n = np.tril(n,-1)
print(n)
print("--- Solucao abaixo falta aprender")

# Crie uma matriz estruturada representando uma posição (x, y) e uma cor (r, g, b)
''' Solucao adaptada da internet: '''
n = np.array(0,[('posicao', [ ('x', float), ('y', float)]),
                ('cor',     [ ('r', float), ('g', float), ('b', float)])])
                
print(n)
print("---")
# Subtrair a média de cada linha de uma matriz
n = np.random.randint(0,10,(3,4))

'''Formato n.mean():
(eixo do array, keepdims=True), onde keepdims=True informa que o resultado
sera salvo num vetor (linha ou coluna) de forma que permita operacoes posteriores
 '''

m = n - n.mean(axis=1, keepdims=True)
print(m)
print("---")

# Como encontrar o valor mais frequente em uma matriz?
n = np.random.randint(1,11,15)
print("Valor mais frequente:", np.bincount(n).argmax())
print("---")

# Crie uma matriz a partir de um arquivo
n = np.fromfile("leiame.txt",dtype=np.int16,sep=" ")
print(n)
print("---")

# crie uma matriz com valores aletaórios e salve para um arquivo
n = np.random.randint(1,11,(5,5))
np.savetxt("n.txt",n)
print("Arquivo salvo com sucesso!")
print("---")

