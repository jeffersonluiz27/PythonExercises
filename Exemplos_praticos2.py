# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 12:11:45 2021

@author: Jefferson
"""

a="Um elefante incomoda muita gente"

a[3:20]

print("Calcule o valor da função Z")
x = int(input("Digite o valor de X: "))
y = int(input("Digite o valor de Y: "))

z = (x**2 + y**2) / ((x - y)**2)

print(z)


print("Calcule o valor do reajuste do salario do funcionario: ")
salario = float(input("Insira o valor com ponto para separar decimais: "))
reajuste = salario + (salario * (35/100))
print("O novo salario com reajuste de 35%% é de R$%.2f reais" % reajuste)


l = [3, 'abacate', 9.7, [5,6,3], "Python", (3,'j')]
print(l[2])
print(l[3])
print(l[3][1])

l[3] = 'morango'
print(l)

l = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
len(l)
min(l)
max(l)
sum(l)
l.append(200)
l.extend([500, 400, 300])
del l[1]
50 in l
l.sort()
l.reverse()

print(l)
