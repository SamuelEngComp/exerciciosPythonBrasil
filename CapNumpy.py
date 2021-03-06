# =============================================================================
# NUMPY
# =============================================================================

import numpy as np

# =============================================================================
# dot -> utilizada para multiplicar vetores
# =============================================================================

lista = np.array([2, 4, 6, 8])
lista02 = np.array([1, 3, 5, 7])
#produto de dois vetores
# exemplo: (2*2)+(4*4)+(6*6)+(8*8) = 120
np.dot(lista, lista)
np.dot(lista, lista02)

# =============================================================================
# shape -> exibir as dimensões de um array no formato de Tuplas
# =============================================================================

# (4,)
lista.shape

# tres dimensões (3,)
lista03 = np.array([1, 2, 3])
lista03.shape

# em matriz
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
    ])

matriz.shape #(3, 3)

# =============================================================================
# slicing
# =============================================================================
#percorrendo os elementos da matriz
matriz[:,2] #todas as linhas da coluna 2
matriz[0] #retorna a 1ª linha da matriz
matriz[1:] #retorna a 2ª e 3ª linha
matriz[1,2] #acessando um elemento especifico

# =============================================================================
# masking
# =============================================================================

#ponto de corte

lista04 = np.array([10, 11, 20, 21, 30, 31, 40, 41, 50, 51, 60, 61])
#neste ponto de corte eu vou definir que todos os numeros com resto da divisão por 2 for zero
#eu vou substituir por 0.

pontoDeCorte = 0
lista04[lista04 % 2 == 0] = pontoDeCorte

#agora a lista deve aparecer alterada
lista04

# =============================================================================
# broadcasting
# =============================================================================
#facilita na operação de arrys de diferentes tamanhos

lista05 = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
    ])

lista05.shape # (3, 2)

lista06 = np.array([10, 100])
lista07 = np.array([
    [10], 
    [100]
    ])


lista06.shape # (2, )
lista07.shape # (2, )

lista08 = lista05*lista06
lista08.shape # (3, 2)

lista05*lista07

lista06[:,None]

# =============================================================================
# dtype
# =============================================================================


























