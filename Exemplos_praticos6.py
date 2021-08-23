# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:20:04 2021

@author: Jefferson
"""

Notas = []

I = 0
while I < 10:
    I = I + 1
    Nota = float(input(f"Entre com {I}ª a nota: "))
    Notas.append(Nota)
    
media = sum(Notas)/len(Notas)
print(f'A média das notas dos alunos é = {media}') 


