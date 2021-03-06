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


def regular (g):
  g1 = grau (g, list(g.keys())[0])
  for v in g:
    g2= grau (g,v)
    if g2!=g1:
      return False
  return True

def grau_grafo (g):
  maior_grau = 0
  for v in g:
    g1 = grau(g,v)
    if g1 > maior_grau:
      maior_grau = g1 

  return maior_grau


def grau(g,v):
  if v in g :
    return len(g[v])
  return -1

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

v = (input('Digite seu vertice para determinar seu grau: '))


x = grau(grafo,v)

if x >= 0:
  print('Grau do vertice', v, "=", x)
else:
  print('Vertice não existe no grafo! ')

if regular(grafo):
  print("Grafo regular!")
else:
  print ("Grafo não é regular")

print ("Grau do grafo =",grau_grafo(grafo))