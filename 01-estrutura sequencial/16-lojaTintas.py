'''
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta 
é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de 
tinta a serem compradas e o preço total.
'''

areaParaSerPintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
lataDeTintas = 18
valorDaLataDeTinta = 80.00

qtdLitrosTinta = areaParaSerPintada / 3
qtdLatasTinta = qtdLitrosTinta/18
precoTotal = qtdLatasTinta*valorDaLataDeTinta

#regra de 3 simples
"""
1 Litro ------>>>>> 3 m^2
x litros ------>>>> area digitada 

1 lata ------>>>>> 18 litros
x latas ----->>>>> qtdLitrosTinta

1 lata  ------>>>> 80
qtdLatasTinta --->>> x

"""

print("Quantidade de latas de tinta a serem compradas: ", qtdLatasTinta, "\n", "Valor total: ", precoTotal, "\n")