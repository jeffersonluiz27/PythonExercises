nomes=[]
while True:
    nome=input("Digite um nome ou 0 para sair: ")
    if nome == "0":
        break
    nomes.append(nome)

print("\nLista usando FOR\n")
for i in nomes:
    print(i)
    
   
print("\nLista usando WHILE\n")
i=0
while i < len(nomes):
    print(nomes[i])
    i+=1

nomes2=nomes[:]

nomes2.append("Antonio")
nomes2.append("Julio")
nomes2.append("Henrique")
nomes2.append("Sabrina")

pesquisa=input("Entre com nome para pesquisar: ")
achou=False
num=0
while num < len(nomes2):
    if pesquisa == nomes2[num]:
        achou=True
        break
    num+=1
if achou == True:
    print("Nome existe")
else:
    print("Nome não encontrado")   
    
for a in nomes2:
    if pesquisa == a:
        print("Achei")
        break
else:
    print("Não achei")
    

