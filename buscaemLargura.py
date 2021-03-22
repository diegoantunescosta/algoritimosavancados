from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = defaultdict(list)

    def  addEdge(self,u,v):
        self.graph[u].append(v)

    def BFS(self,s):

        visitado = [False] * (len(self.graph))

        fila = []

        fila.append(s)
        visitado[s] = True

        while fila:

            s= fila.pop(0)
            print(s)

            for i in self.graph[s]:
                # print(visitado[i])
                if visitado[i] == False:
                    fila.append(i)
                    visitado[i] = True

g = Graph()
g.addEdge(0,2)
g.addEdge(0,3)
g.addEdge(0,4)
g.addEdge(1,2)
g.addEdge(1,4)
g.addEdge(2,4)
g.addEdge(3,4)
g.addEdge(3,5)
g.addEdge(4,5)
g.addEdge(5,1)

print("Retorno da execucao da busca em largura: ")
g.BFS(0)
        
        