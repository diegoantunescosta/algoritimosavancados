def Push(P, t, val):
    P.insert(t, val)

def Pop(P):
    P.pop()

Pilha = []
topo=-1
bin = 0

num = int(input("Digite um número em decimal: "))

while (num > 0):
    resto = num % 2
    Push(Pilha, topo, resto)
    topo += 1
    num = num // 2

while (topo >= 0):
    bin = bin * 10 + Pilha[topo]
    Pop(Pilha)
    topo -= 1

print("Valor em binario = ", bin)

  