import numpy as np

class listaNumpy():
    __arq = ''
    __txt = []

    #def __init__(self):

    def createnullvector(self,size):
        # Crie um vetor nulo de determinado tamanho
        vec = np.zeros(size)
        return vec

    def memory(self,matrix):
        # Encontra o tamanho da memória de qualquer matriz
        print("Memory layout:\n", matrix.flags)
        print("Total consumed bytes:\n", matrix.nbytes)

    def createonevector(self,size,position):
        # Crie um vetor nulo de tamanho 'size', mas o 'position' valor, que é 1
        vec = self.createnullvector(size)
        vec[position-1] = 1
        return vec

    def createrangevector(self,size,min,max):
        # Crie um vetor, de tamanho 'size', com valores que variam de 0 a 'value'
        vec = np.random.random_integers(min, max, size)
        return vec

    def flipvector(self,vector):
        # Inverter um vetor (o primeiro elemento se torna o último)
        vec = np.flip(vector)
        return(vec)

    def matrix(self,n,min=0,max=0):
        # Crie uma matriz nxn com valores que variam de min a max
        mt = np.array([self.createrangevector(n, min, max) for i in range(n)])
        return mt

    def indexnotzero(self,array):
        # Encontre índices de elementos diferentes de zero em um array
        return np.nonzero(array)

    def mtident(self,n):
        # Crie uma matriz de identidade nxn
        return np.identity(n)

    def matriz3D(self,n):
        # Crie uma matriz nxnxn com valores aleatórios
        return np.array([[np.random.rand(n) for i in range(n)]for a in range(n)])

    def matrixrange(self,n):
        # Crie uma matriz 10x10 com valores aleatórios e encontre os valores mínimo e máximo
        mt = np.array([np.random.rand(2) for i in range(n)])
        return mt, np.min(mt), np.max(mt)

    def matrixmean(self,n):
        # Crie um vetor aleatório de tamanho 30 e encontre o valor médio
        mt = np.random.rand(n)
        return mt, np.mean(mt)

    def nullcenter(self,size):
        # Crie uma matriz 2D com 1 na borda e 0 dentro
        mt = np.array([np.ones(size)for i in range(size)])
        mt[1:-1,1:-1]=0
        return mt

    def matrix5(self):
        # Crie uma matriz 5x5 com valores 1,2,3,4 logo abaixo da diagonal
        mt = np.array([np.zeros(5) for i in range(5)])
        for i in range(1,len(mt)):
            mt[len(mt)-i][i]=i
        return mt

    def structmt(self, r = (0,0), g = (0,1), b = (0,2)):
        # Crie uma matriz estruturada representando uma posição (x, y) e uma cor (r, g, b)
        return np.array([('r', r), ('g', g), ('b', b)])

    def submean(self,array):
        # Subtrair a média de cada linha de uma matriz
        return [vec - np.mean(vec) for vec in array]

    def matrixmode(self,array):
        # Como encontrar o valor mais frequente em uma matriz?
        counts = np.bincount(array)
        return np.argmax(counts)

    def createmx(self,path):
        # Crie uma matriz a partir de um arquivo
        return np.loadtxt(path)

    def savemx(self,path,n=2):
        # Crie uma matriz com valores aletaórios e salve para um arquivo
        np.savetxt(path,np.eye(n))
        print("Arquivo salvo com sucesso em %s" % path)



obj = listaNumpy()

#vetor = obj.createnullvector(10)
#obj.memory(vetor)
#print(obj.createonevector(10,5))
#vetora = obj.createrangevector(10,10,49)
#print(vetora)
#print(obj.flipvector(vetora))
#print(obj.matrix(3,max=8))
#ar = [1,2,0,0,4,0]
#print(obj.indexnotzero(ar))
#print(obj.mtident(3))
#print(obj.matriz3D(3))
#print(obj.matrixrange(10))
#print(obj.matrixmean(30))
#print(obj.nullcenter(6))
#print(obj.matrix5())
#print(obj.structmt(r=(1,2), g = (1,0)))
#print(obj.submean([[1,1,1],[2,2,2],[3,3,3]]))
#print(obj.matrixmode([0,0,1,1,3,2,3,2,3]))
#print(obj.createmx('/home/alessandra/PycharmProjects/tensorEnv/matriz.txt'))
#obj.savemx('/home/alessandra/PycharmProjects/tensorEnv/result.txt')