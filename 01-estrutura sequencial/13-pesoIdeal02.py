# =============================================================================
# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
# A) Para homens: (72.7*h) - 58
# B) Para mulheres: (62.1*h) - 44.7
# =============================================================================
alturaPessoa = float(input("digite a altura da pessoa: "))
pesoIdealHomens = (72.7*alturaPessoa) - 58
pesoIdealMulheres = (62.1*alturaPessoa) - 44.7

#A)
print("Peso ideal HOMENS: ", pesoIdealHomens)

#B)
print("Peso ideal MULHERES: ", pesoIdealMulheres)