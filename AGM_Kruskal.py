from math import inf

def dijkstra(Grafo, V, distacia_acumulada, antes, amplia, inicio, chegada):
    x = inicio

    while x!= chegada:
        for adjacent in Grafo[x]:
            if adjacent[0] not in amplia:
                if x == inicio:
                    acum = 0
                else:
                    acum = distacia_acumulada[V.index(x)]
                if (acum + adjacent[1] < distacia_acumulada[V.index(adjacent[0])]):
                    distacia_acumulada[V.index(adjacent[0])] = acum+adjacent[1]
                    antes[V.index(adjacent[0])] = x
        amplia.append(x)
        j = float('inf')
        for i in range(len(distacia_acumulada)):
            if (V[i] not in amplia and distacia_acumulada[i] < j):
                j = distacia_acumulada[i]
                x = V[i]


def imprimirCaminho (inicio, chegada, antes, V ):
    X = chegada
    cam = []
    cam.append(X)
    while X != inicio:
        X = antes[V.index(X)]
        cam.insert(0, X)

    print(cam)


Grafo = {'A':[['B',2],['C',3], ['E',6],['K',4]],
         'B':[['A',2], ['D',9]],
         'C':[['A',3],['K',9],['H',5]],
         'D':[['B',9],['F',6]],
         'E':[['A',6], ['K',7], ['F',8]],
         'F':[['E',8],['G',5],['D',6]],
         'G':[['H',3],['I',11],['K',10],['F',5]],
         'H':[['C',5],['G',3],['J',2]],
         'I':[['G',11],['J',3]],
         'J':[['I',3],['H',2]],
         'K':[['A',4],['C',9],['E',7],['G',10]]
         }
# Nomeando as posições do vetor
V = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K"]
# vetor de distâncias acumuladas
distacia_acumulada = [0]*11
for i in range (11):
    distacia_acumulada[i] = (float(inf))
# Vetor para anteriores
antes = [0]*11
# vertor para expandidos
amplia = []


inicio = input("Digite o vértice de inicio (A a K):")
chegada = input("Digite o vértice chegada (A a K):")
if inicio == chegada:
    print("O vértice origem deve ser diferente do de chegada.")
else:

    dijkstra(Grafo, V, distacia_acumulada, antes, amplia, inicio, chegada)

    imprimirCaminho(inicio, chegada, antes, V)





