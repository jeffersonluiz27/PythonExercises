# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:48:02 2021

@author: Jefferson
"""

def maior (x,y):
    if x>y:
        print(x)
    else:
        print(y)

def line(x):
    print('_'*x)
    
def linha(N):
    for i in range(N):
        print(end='_')
    print(" ")


def imprime_lista(L):
    contador=0
    for valor in L:
            contador = contador + 1
            print(contador,')',valor)
            
def media_lista(L):
    somador=0
    for valor in L:
            somador = somador + valor
    return somador/len(L)

L = int(input("Digite o Tamanho da linha: "))

line(L)    

maior(4, 7)

linha(L)

lista = ['A', 'B','C','D','E']
imprime_lista(lista)

lista2 = [1,2,3,4,5]
print(f'A media dos valores = {media_lista(lista2)}')
