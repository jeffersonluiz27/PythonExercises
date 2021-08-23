# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 10:56:36 2021

@author: Jefferson
"""

print("Insira 2 nota e descubra se foi aprovado")
nota1 = int(input("Entre com a primeira nota: "))
nota2 = int(input("Entre com a segunda nota: "))

media = (nota1+nota2)/2

if media >= 6:
    print("Aprovado")
else:
    print("Reprovado")
    

media2 = media

if media2 > 6:
    print("Aprovado")
elif media2 < 4:
    print("Reprovado")
else:
    print("Exame")