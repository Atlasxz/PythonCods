# -*- coding: utf-8 -*-
"""3 - Verificação salarial - Lista 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zu7bi3AKBuTbS7Ser86PHAiiYC606lPv
"""

Sal = int(input('Digite seu salário: '))
Gasto = int(input('Digite seu gasto total: '))
Lucro = (Sal-Gasto)
if (Lucro>=0):
  print('Orçamento dentro do esperado')
else:
  print('Orçamento estourado, revise os gastos')

print(f"Seu saldo é: {Lucro}")