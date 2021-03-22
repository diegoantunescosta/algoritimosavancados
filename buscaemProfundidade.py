grafo= {"A": ["B", "C"],
        "B": ["E", "A"],
        "C": ["E"],
        "D": ["H", "G"],
        "E": ["I", "F", "C", "B"],
        "F": ["E", "I"],
        "G": ["D", "K", "J"],
        "H": ["K", "D"],
        "I": ["J", "F", "E"],
        "J": ["G", "L", "I"],
        "K": ["G", "H"],
        "L": ["J"],
        }

pilha = []
marcados = []
visitados = []
topo = -1


def Push(pilha, topo, v):
    pilha.insert(topo, v)


def Pop(pilha):
    pilha.pop()


def busca_prof(grafo, pilha, topo, v):
    marcados.append(v)
    visitados.append(v)
    Push(pilha, topo, v)
    topo += 1

    while topo >= 0:
        n = pilha[topo - 1]
        Pop(pilha)
        topo -= 1

        for m in grafo[n]:
            if m not in marcados:
                visitados.append(m)
                Push(pilha, topo, n)
                topo += 1
                Push(pilha, topo, m)
                topo += 1
                marcados.append(m)
                n = m



while True:
    v = input("Digite o vertice:")
    busca_prof(grafo,pilha,topo,v)

    print("O grafo apresentado para o programa foi: ", grafo)
    print("Os vertices marcados foram:", marcados)
    print("Os vertices visitados foram: ", visitados)
    print(" A relacao dessa pilha ficou disposta dessa forma: ", pilha)
    resp = input("Deseja verificar mais algum caminho? (S ou N):")
    if resp == 'N':
        break

    #créditos ao Carlos Nobuaki