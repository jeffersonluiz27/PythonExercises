# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 13:40:22 2021

@author: Jefferson
"""

num = int(input("Digite o numero de 1 a 10 para receber a tabuada: "))
print("Tabuada do ", num)

for x in range(1,11):
    print(f"{num} X {x} = {num*x}")
