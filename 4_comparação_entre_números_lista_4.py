# -*- coding: utf-8 -*-
"""4 - Comparação entre números - Lista 4

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uHzFSQHGLHnsPVjFFyJ4F_vHzBZPE6WR
"""

NumberOne = int(input('Digite um número para comparação com outro: '))
NumberTwo = int(input('Digite outro número para comparação o primeiro: '))

if NumberOne > NumberTwo:
  print('O número {}, é maior que {}'.format(NumberOne,NumberTwo))

if NumberTwo > NumberOne:
  print('O número {}, é maior que {}'.format(NumberTwo,NumberOne))