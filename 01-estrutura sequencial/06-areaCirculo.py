# =============================================================================
# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
# =============================================================================
import math as ma

raio = float(input("digite o valor do raio: "))
areaDoCirculo = ma.pi * ma.pow(raio, 2)
print("Area do circulo: ", areaDoCirculo)
