# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:03:02 2021

@author: Jefferson
"""

senha = "54321"
leitura = ""
while (leitura != senha):
    leitura = input("Degite a senha: ")
    if leitura == senha:
        print("Acesso Liberado")
    else:
        print("Senha incorreta. Tente novamente!")
        
        
contador = 0
somador = 0

while contador < 5:
    contador = contador + 1
    valor = float(input('Digite o '+str(contador)+'º Valor: '))
    somador = somador + valor
print(f'Soma = {somador}')


S=0
for x in range(3,334,3):
    S=S+x
    print(x)
print(f'Soma = {S}')

