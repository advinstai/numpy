#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 13:37:57 2019

@author: felipe


  OBS.: Os demais exercícios (do arquivo readme.md) estáo no final deste arquivo

    Crie um vetor nulo de tamanho 10
    Como encontrar o tamanho da memória de qualquer matriz
    Crie um vetor nulo de tamanho 10, mas o quinto valor, que é 1
    Crie um vetor com valores que variam de 10 a 49
    Inverter um vetor (o primeiro elemento se torna o último)
    Crie uma matriz 3x3 com valores que variam de 0 a 8
    Crie uma matriz de identidade 3x3
    Crie uma matriz 3x3x3 com valores aleatórios
    Crie uma matriz 10x10 com valores aleatórios e encontre os valores mínimo e máximo
    Crie um vetor aleatório de tamanho 30 e encontre o valor médio
    Crie uma matriz 2D com 1 na borda e 0 dentro
    Crie uma matriz 5x5 com valores 1,2,3,4 logo abaixo da diagonal
    Crie uma matriz estruturada representando uma posição (x, y) e uma cor (r, g, b)
    Subtrair a média de cada linha de uma matriz
    Como encontrar o valor mais frequente em uma matriz?
    Crie uma matriz a partir de um arquivo
    crie uma matriz com valores aletaórios e salve para um arquivo

"""

import numpy as np

import random as rnd

rnd.seed(29102019);

#%% Crie um vetor nulo de tamanho 10
vetor = np.zeros(10)
# ou
vetor = np.empty(10)

#%% Como encontrar o tamanho da memória de qualquer matriz
mem = len (vetor.tobytes())

mem = len (vetor.flatten().tobytes())

#%% Crie um vetor nulo de tamanho 10, mas o quinto valor, que é 1
vetorN = np.zeros(10); vetorN[4] = 1

vetorN = np.heaviside(range(-4,6),2) // 2

#%% Crie um vetor com valores que variam de 10 a 49

vetorA = np.random.randint(10,49,10)

#%%   Inverter um vetor (o primeiro elemento se torna o último)
vetorI = vetorA[::-1]

#%% Crie uma matriz 3x3 com valores que variam de 0 a 8

vetorC = np.random.randint(0,8,(3,3))

#%% Crie uma matriz de identidade 3x3

matrizI = np.identity(3)

#%%  Crie uma matriz 3x3x3 com valores aleatórios

vetorC = np.random.randint(0,8,(3,3,3))

#%%  Crie uma matriz 10x10 com valores aleatórios e encontre os valores mínimo e máximo

matrizC = np.random.randint(0,8,(10,10))

maxVetorCa = np.max(matrizC)

maxVetorCb = max(matrizC.flatten())

minVetorCa = np.min(matrizC)

minVetorCb = min(matrizC.flatten())


#%% Crie um vetor aleatório de tamanho 30 e encontre o valor médio

vetorRnd = np.random.randint(0,10,30)

menaVetorRnd = np.mean(vetorRnd)

#%% Crie uma matriz 2D com 1 na borda e 0 dentro

matrizA = np.zeros((5,5))

matrizA[0,:] = 1
matrizA[-1,:] = 1
matrizA[:,0] = 1
matrizA[:,-1] = 1

# ou:

matrizA = np.ones((5,5)) 

# mascara (cria matriz tamanho n/m -2)
matrizC = np.zeros(( matrizA.shape[0] -2, matrizA.shape[1]-2))

matrizA[1:-1:,1:-1:] = matrizC #aplica a mascara com deslocamento de 1 abaixo

matrizD = np.zeros((5,5))

#%% Crie uma matriz 5x5 com valores 1,2,3,4 logo abaixo da diagonal

matrizL= np.zeros((4,4))

np.fill_diagonal(matrizL, range(1,5))

matrizM = np.zeros((5,5))

matrizM[1:,0:-1] = matrizL


#%% Crie uma matriz estruturada representando uma posição (x, y) e uma cor (r, g, b)

dim = (10,10)
matrizEstruturada = np.zeros(dim, dtype=tuple)
matrizEstruturada.fill(( 'r', 'g', 'b' ))

#%% Subtrair a média de cada linha de uma matriz

matrizT = np.random.randint(0,10,dim)

mean = np.mean(matrizT,1)

#média dos pares de linhas:
meanT =  np.mean(np.reshape(mean,(5,2)),1)

# %% Como encontrar o valor mais frequente em uma matriz?
  
matrizH = np.random.randint(0,10,dim)

f,b = np.histogram(matrizH, range(0,11))

maisFrequente = max(zip(f,b))

# %%   Crie uma matriz a partir de um arquivo
#      Crie uma matriz com valores aletaórios e salve para um arquivo

np.savetxt("matrizA.dat", matrizA)

recuperaMatriz = np.loadtxt("matrizA")

matrizK = np.random.randint(0,10,(5,5))

np.savetxt("matrizRnd.dat", matrizK)


# %% Outros

"""


    Crie um array com 10 elementos usando a função arange

    Transforme esse array de 1D (1x10) para 2D (2x5) usando a função reshape

    Crie duas matrizes bidimensionais com valores aleatórios

    calcule a transposta de cada matriz

    multiplique as duas matrizes

    Salve as matrizes de entrada e a de saída em arquivos. Qual o tamanho dos arquivos gerados?

    Crie duas bidimensionais matrizes com valores aleatórios e gere uma única matriz combinando linha a linha
"""


mm1 = np.arange(10)

mm2 = np.reshape(mm1, (2,5))

magic = lambda n : np.random.randint(-100,100,n)

mm3 = magic((10,10))

mm4 = magic((10,10))

mx = np.dot(mm3,mm4)

mm3t, mm4t  = ( np.transpose(mm3) , np.transpose(mm4) )

mm5 = np.zeros((2,10,10))

mm5[0:,:,:] = mm3
mm5[1:,:,:] = mm4

np.savetxt("matrizmm.dat", mm3)

#o tamanho é de 2.5 kB, um valor relativamente grande, pois é salvo em string literal
#na notaçao científica





