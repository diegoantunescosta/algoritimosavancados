def Push(P, t, val):
    P.insert(t, val)

def Pop(P):
    P.pop()

Pilha = []

topo=-1
bin = 0

palavra = (input('Digite uma palavra : '))

for letra in palavra:
  topo += 1
  Push (Pilha,topo,letra )



inv = ''
# enquanto houver letras na pilha
while (topo >= 0):
  letra = Pilha[topo]
  inv += letra
  Pop(Pilha)
  topo -=1

print('Palavra Lida = ',palavra)
print('Palavra Invertida = ',inv)

if (palavra == inv):
  print ('Esta palavra é palindromo !')
else:
  print ('Não é palindromo !')