# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 14:47:45 2021

@author: Jefferson
"""

l = [5, 7, 2, 9, 4, 1, 3]
len(l)
max(l)
min(l)
sum(l)
l.sort()
print(l)
l.reverse()
print(l)

L1 = list(range(0,50,3))
print(L1)

Tupla = (10, 20, 30, 40, 50)
a,b,c,d,e = Tupla
print("A = ", a," e D = ",d)
print("D + E = ", d+e)

# Uma tupla é imutavel portanto não é possível fazer essa atribuição --> Tupla[2]=8

Nome_dicionario = {
    "arroz" : 17.30,
    "feijão" : 12.50,
    "carne" : 23.90,
    "alface" : 3.40
    }

print(Nome_dicionario)

print(Nome_dicionario["carne"])

del Nome_dicionario["feijão"]
print(Nome_dicionario)

"batata" in Nome_dicionario
"alface" in Nome_dicionario

Nome_dicionario.keys()
Nome_dicionario.values()


Lanchonete = {
    "Salgado": 4.50,
    "Lanche": 6.50,
    "Suco": 3.00,
    "Refrigerante": 3.50,
    "Doce": 1.00
    }

print(Lanchonete)

Boletim = {
    "João": 5.0,
    "Lucas": 7.0,
    "Vitor": 8.5,
    "Luana": 4.5,
    "Luiza": 9.0
    }


Media = sum(Boletim.values()) / len(Boletim)
print(Media)

Boletim["Antonio"] = 8.0

print(Boletim)

Media = sum(Boletim.values()) / len(Boletim)
print(Media)
