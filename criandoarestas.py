def inserir(g, a, b):
  if a not in g:
    g[a]=[]
  if b not in g:
    g[b] = []

  g[a].append(b)
  g[b].append(a)

def imprimir(g):
  for v,a in g.items():
    print ('Vertice:',v)
    print ('Adjacentes',a)
    print ('-'* 10)

def adjacentes(g,v):
  if v in g:
    print ("Adjacentes de ",v,"=", g[v])
  else: 
    print("O vertice ",v," não existe no grafo")

grafo = {}

while True:
 print('Digite a aresta na forma V1 -- V2:')
 x = input()
 y = input ()
 inserir(grafo, x,y)
 resp = input('Deseja inserir mais arestas ? (S ou N)')
 if resp == 'N':
   break

imprimir(grafo)

v = (input('Digite o vertice que deseja ver: '))

adjacentes(grafo,v)

# opcao = (input('digite a vertice:'))
# print (grafo[opcao])