
def ins_aresta(g,x,y):
  if x not in g:
    g[x] = []
  if y not in g:
    g[y] = []
  g[x].append(y)


grafo = {}
vertice = []

while True:
  x = input ('Digite o vertice de origem (ou FIM): ')
  if x =='FIM':
    break

  y = input ('Digite o vertice de destino: ')
  if x not in vertice:
    vertice.append(x)
  if y not in vertice:
    vertice.append(y)
  ins_aresta (grafo,x,y)

print (grafo)
print('Vertices: ', vertice)