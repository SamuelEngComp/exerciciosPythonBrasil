'''
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, 
que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

    ------------->>>> comprar apenas latas de 18 litros;
    ------------->>>> comprar apenas galões de 3,6 litros;
    ------------->>>> misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde 
                    os valores para cima, isto é, considere latas cheias.
'''

areaParaSerPintada = float(input("Digite o tamanho em metros quadrados da área a ser pintada: "))
lataDeTintas = 18
galoesDeTintas = 3.6
valorDaLataDeTinta = 80.00
valorDoGalaoDeTinta = 25.00

qtdLitrosTinta = areaParaSerPintada / 6
qtdLatasTinta = qtdLitrosTinta/18
qtdGaloesDeTinta = qtdLitrosTinta/3.6
precoLatasDeTinta = qtdLatasTinta * valorDaLataDeTinta
precoGaloesDeTinta = qtdGaloesDeTinta * valorDoGalaoDeTinta

# so compensa comprar latas de tintas se tiver 108 m^2
if areaParaSerPintada >= 108:
    print("compre lata de 18 litros de tinta")
elif areaParaSerPintada >= 21.6 and areaParaSerPintada < 108:
    print("compre galoes de 3.6 litros de tinta")
else:
    print("compre 1 galao de 3.6 litros de tinta")
