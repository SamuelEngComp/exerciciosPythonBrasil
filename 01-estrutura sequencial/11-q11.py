# =============================================================================
# Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
# a) o produto do dobro do primeiro com metade do segundo .
# b) a soma do triplo do primeiro com o terceiro.
# c) o terceiro elevado ao cubo.
# =============================================================================

primeiroNumeroInteiro = int(input("digite o primeiro numero INTEIRO: "))
segundoNumeroInteiro = int(input("digite o segundo numero INTEIRO: "))
primeiroNumeroReal = float(input("digite um numero REAL: "))

#A)
produtoDoDobro = (2*primeiroNumeroInteiro)*(segundoNumeroInteiro/2)

#B)
soma = 3*primeiroNumeroInteiro + primeiroNumeroReal

#C
cubo = primeiroNumeroReal**3

print("A: ", produtoDoDobro, "B: ", soma, "C: ", cubo)