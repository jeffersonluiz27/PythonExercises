
# FIFO

passageiros=["Jose","Luiz","Ana","Sandra","Rosa","Roberto"]
ultimo=len(passageiros)

while True:
    print("Tem %d passageiros na fila :" % ultimo,"\nE eles são: ", passageiros)
    acao = int(input("Digite 1 para inclur\nDigite 2 para retirar\nDigite 0 para sair\n:"))
    if acao == 1:
        pessoa = input("Digite o nome da pessoa que entrou na fila: ")
        passageiros.append(pessoa)
        ultimo+=1
    elif acao == 2:
        if len(passageiros) > 0:
            passageiros.pop(0)
            ultimo-=1
        else:
            print("\nFila Vazia!\n")
    elif acao == 0:
        break
    

#LIFO
    
panquecas=["Panqueca1","Panqueca2","Panqueca3","Panqueca4","Panqueca5","Panqueca6"]
ultima=len(panquecas)

while True:
    print("Tem %d panquecas no prato :" % ultima,"\nE elas são: ", panquecas)
    acao = int(input("Digite 1 para inclur\nDigite 2 para retirar\nDigite 0 para sair\n:"))
    if acao == 1:
        panquecas.append("Panqueca %d" % (ultima+1))
        ultima+=1
    elif acao == 2:
        if len(panquecas) > 0:
            panquecas.pop(-1)
            ultima-=1
        else:
            print("\nNão tem mais panquecas\n")
    elif acao == 0:
        break
    
