# =============================================================================
# Faça um Programa que peça as 4 notas bimestrais e mostre a média
# =============================================================================
primeiraNota = float(input("digite a primeira nota: "))
segundaNota = float(input("digite a segunda nota: "))
terceiraNota = float(input("digite a terceira nota: "))
quartaNota = float(input("digite a quarta nota: "))

soma = primeiraNota + segundaNota + terceiraNota + quartaNota
media = soma / 4

print("A media eh: ", media)

"""
if media >= 7:
    print("aprovado")
elif media <= 6.9 and media >= 5:
    print("recuperacao")
else:
    print("reprovado")
    
"""