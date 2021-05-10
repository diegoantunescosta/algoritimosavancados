nomes = []
nomes_repetidos = []

while True: 
  
  input_nome = input('Digite seu primeiro nome ou FIM para sair : ')
  
  if input_nome == 'FIM':
    break

  if input_nome in nomes:
    nomes_repetidos.append(input_nome)

  if input_nome not in nomes:
    nomes.append(input_nome)
  
 
    

print ('Nomes cadastrados na lista', nomes)
print ('Nomes cadastrados repetidamente na lista', nomes_repetidos)

