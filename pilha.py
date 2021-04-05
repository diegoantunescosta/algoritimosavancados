def Push (P,t, val):
  P.insert(t,val)

def Remove (P):
  P.pop()

def Imprime (P,t):
  for i in range (t,-1, -1):
    print ("[",P[i],"]")



# Topo == -1
Pilha = []
topo = -1

while True:
  num = int( input ("Digite um valor na Pilha ou digite 0 para sair: "))
  if num == 0:
    break
  
  topo += 1
  Push(Pilha,topo,num)


Imprime(Pilha, topo)

# metodo para remover valor da Pilha


if (topo>= 0):
  print ("O valor", Pilha[topo],"será removido!")
  Remove(Pilha)
  topo -=1
else:
  print("Pilha vazia")

print('Pilha após remoção: ')
Imprime(Pilha, topo)