# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:08:45 2021

@author: Jefferson
"""

Feira = {}

Feira["Abacate"] = 1.99
Feira["Manga"] = 2.29
Feira["Coco"] = 5.25
i=0
for x in Feira:
    i=i+1
    print(f' Item {i} = {x} : R$ {Feira[x]:,}')
print(f'Total do carrinho = R$ {sum(Feira.values()):,.2f}')