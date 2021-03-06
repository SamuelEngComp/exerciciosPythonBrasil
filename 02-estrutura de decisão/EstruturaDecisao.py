# =============================================================================
# Exercicios de estrutura de decisÃ£o - Site Python Brasil
# =============================================================================

# =============================================================================
# 01 - FaÃ§a um Programa que peÃ§a dois nÃºmeros e 
# imprima o maior deles.
# =============================================================================

import numpy as np

numero01 = float(input("Dgite o primeiro numero: "))
numero02 = float(input("Dgite o segundo numero: "))

# utilizando numpy
maiorNumero = np.array([numero01, numero02])
numeroMaior = maiorNumero.max()
print("O numero: ", numeroMaior, " eh o maior numero digitado")

#utilizando as condicionais IF ELSE
if numero01 > numero02:
    print("O numero: ", numero01, " eh o maior numero digitado")
elif numero02 > numero01:
    print("O numero: ", numero02, " eh o maior numero digitado")
else:
    print("Os numeros sao iguais !!!")
    
    
    
    
# =============================================================================
# 02 - Faça um Programa que peça um valor e mostre na tela 
# se o valor é positivo ou negativo
# =============================================================================

numeroPositivo = float(input("Dgite um numero: "))
if numeroPositivo < 0:
    print("Numero negativo")
else:
    print("numero positivo")
    

# =============================================================================
# 03 - Faça um Programa que verifique se uma letra 
# digitada é "F" ou "M". Conforme a letra escrever: 
#   F - Feminino, M - Masculino, Sexo Inválido
# =============================================================================

letraDigitada = input("Digite uma letra: ")
letraDigitada = letraDigitada.upper()
if len(letraDigitada) == 1:
    if letraDigitada == 'F':
        print("sexo feminino")
    elif letraDigitada == 'M':
        print("sexo masculino")
    else:
        print("Sexo invalido")
else:
    print("digitacao invalida")


# =============================================================================
# 04 - Faça um Programa que verifique se uma letra 
#      digitada é vogal ou consoante.
# =============================================================================

vogais = ['a','e','i','o','u']
consoantes = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','y','z']
digito = input("digite uma letra: ")
digito = digito.lower()

if digito in vogais:
    print("eh uma vogal: ", digito)
elif digito in consoantes:
    print("eh uma consoante: ", digito)
else:
    print("eh um numero ")
    
# =============================================================================
# 05 - Faça um programa para a leitura de duas notas parciais de um aluno. 
# O programa deve calcular a média alcançada por aluno e apresentar:
#   *A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;   
#   *A mensagem "Reprovado", se a média for menor do que sete;
#   *A mensagem "Aprovado com Distinção", se a média for igual a dez.
# =============================================================================

nota01 = float(input("Digite a primeira nota: "))
nota02 = float(input("Digite a segunda nota: "))
media = (nota01+nota02)/2
if media >= 7.0 and media < 10.0:
    print("Aprovado")
elif media < 7.0:
    print("Reprovado")
elif media == 10:
    print("Aprovado com Distinção")
    
# =============================================================================
# 06 - Faça um Programa que leia três números e mostre o maior deles.
# =============================================================================

numero01 = float(input("digite o primeiro numero: "))
numero02 = float(input("digite o segundo numero: "))
numero03 = float(input("digite o terceiro numero: "))

# novamente utilizando numpy
#maior = np.array([numero01, numero02, numero03])
#maiorNumero = maior.max()

if (numero01 > numero02 and numero02 > numero03) or (numero01 > numero02 and numero03 < numero01):
    print("numero: ", numero01, " eh maior")
if (numero02 > numero01 and numero01 > numero03) or (numero02 > numero01 and numero03 < numero02):
    print("numero: ", numero02, " eh maior")
if (numero03 > numero02 and numero02 > numero01) or (numero03 > numero01 and numero02 < numero01):
    print("numero: ", numero03, " eh maior")

# =============================================================================
# 07 - Faça um Programa que leia três números e mostre o maior e o menor deles
# =============================================================================

numero01 = float(input("digite o primeiro numero: "))
numero02 = float(input("digite o segundo numero: "))
numero03 = float(input("digite o terceiro numero: "))

"""
maior = np.array([numero01, numero02, numero03])
maiorNumero = maior.max()
menorNumero = maior.min()
"""

if (numero01 > numero02 and numero02 > numero03):
    print("numero: ", numero01, " eh maior")
    print("numero: ", numero03, " eh menor")
if (numero01 > numero03 and numero03 > numero02):
    print("numero: ", numero01, " eh maior")
    print("numero: ", numero02, " eh menor")
if (numero02 > numero01 and numero01 > numero03): 
    print("numero: ", numero02, " eh maior")
    print("numero: ", numero03, " eh menor")
if (numero02 > numero03 and numero03 > numero01):
    print("numero: ", numero02, " eh maior")
    print("numero: ", numero01, " eh menor")
if (numero03 > numero02 and numero02 > numero01):
    print("numero: ", numero03, " eh maior")
    print("numero: ", numero01, " eh menor")
if (numero03 > numero01 and numero01 > numero02):
    print("numero: ", numero03, " eh maior")
    print("numero: ", numero02, " eh menor")


# =============================================================================
# 08 - Faça um programa que pergunte o preço de três produtos e informe qual produto 
# você deve comprar, sabendo que a decisão é sempre pelo mais barato.
# =============================================================================

preco1 = float(input("digite o preco 1: "))
preco2 = float(input("digite o preco 2: "))
preco3 = float(input("digite o preco 3: "))
"""
maior = np.array([preco1, preco2, preco3])
maiorPreco = maior.max()
menorPreco = maior.min()
"""
if (preco1 > preco2 and preco2 > preco3):
    #print("numero: ", numero01, " eh maior")
    print("Produto mais barato: ", preco3)
if (preco1 > preco3 and preco3 > preco2):
    #print("numero: ", numero01, " eh maior")
    print("Produto mais barato: ", preco2)
if (preco2 > preco1 and preco1 > preco3): 
    #print("numero: ", numero02, " eh maior")
    print("Produto mais barato: ", preco3)
if (preco2 > preco3 and preco3 > preco1):
    #print("numero: ", numero02, " eh maior")
    print("Produto mais barato: ", preco1)
if (preco3 > preco2 and preco2 > preco1):
    #print("numero: ", numero03, " eh maior")
    print("Produto mais barato: ", preco1)
if (preco3 > preco1 and preco1 > preco2):
    #print("numero: ", numero03, " eh maior")
    print("Produto mais barato: ", preco2)

# =============================================================================
# 09 - Faça um Programa que leia três números e mostre-os em ordem decrescente
# =============================================================================

preco1 = float(input("digite o preco 1: "))
preco2 = float(input("digite o preco 2: "))
preco3 = float(input("digite o preco 3: "))

"""
maior = np.array([preco1, preco2, preco3])
maiorPreco = maior.max()
menorPreco = maior.min()
print(-np.sort(-maior)) #utilizar o sinal negativo para ordenar o vetor de forma decrescente
"""
ordemDecrescente = []

if (preco1 > preco2 and preco2 > preco3):
    #print("numero: ", preco1, " eh maior")
    #print("Produto mais barato: ", preco3)
    ordemDecrescente.append(preco1)
    ordemDecrescente.append(preco2)
    ordemDecrescente.append(preco3)
    print("Ordem Decrescente: ", ordemDecrescente)
if (preco1 > preco3 and preco3 > preco2):
    #print("numero: ", preco1, " eh maior")
    #print("Produto mais barato: ", preco2)
    ordemDecrescente.append(preco1)
    ordemDecrescente.append(preco3)
    ordemDecrescente.append(preco2)
    print("Ordem Decrescente: ", ordemDecrescente)
if (preco2 > preco1 and preco1 > preco3): 
    #print("numero: ", preco2, " eh maior")
    #print("Produto mais barato: ", preco3)
    ordemDecrescente.append(preco2)
    ordemDecrescente.append(preco1)
    ordemDecrescente.append(preco3)
    print("Ordem Decrescente: ", ordemDecrescente)
if (preco2 > preco3 and preco3 > preco1):
    #print("numero: ", preco2, " eh maior")
    #print("Produto mais barato: ", preco1)
    ordemDecrescente.append(preco2)
    ordemDecrescente.append(preco3)
    ordemDecrescente.append(preco1)
    print("Ordem Decrescente: ", ordemDecrescente)
if (preco3 > preco2 and preco2 > preco1):
    #print("numero: ", preco3, " eh maior")
    #print("Produto mais barato: ", preco1)
    ordemDecrescente.append(preco3)
    ordemDecrescente.append(preco2)
    ordemDecrescente.append(preco1)
    print("Ordem Decrescente: ", ordemDecrescente)
if (preco3 > preco1 and preco1 > preco2):
    #print("numero: ", preco3, " eh maior")
    #print("Produto mais barato: ", preco2)
    ordemDecrescente.append(preco3)
    ordemDecrescente.append(preco1)
    ordemDecrescente.append(preco2)
    print("Ordem Decrescente: ", ordemDecrescente)

# =============================================================================
# 10 - Faça um Programa que pergunte em que turno você estuda. 
#    Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
#   Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
# =============================================================================

print("Digite o turno que vc estuda ")
turnoDeEstudo = input("M - Matutino\n V - Vespertino\n N - Noturno\n")

turnoDeEstudo = turnoDeEstudo.lower()

if turnoDeEstudo == 'm':
    print("Bom dia !")
elif turnoDeEstudo == 'v':
    print("Boa tarde !")
elif turnoDeEstudo == 'n':
    print("Boa noite !")
else:
    print("Valor invalido !")
    
    
# =============================================================================
# 11 - As Organizações Tabajara resolveram dar um aumento de salário aos seus 
# colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
#       
#        Faça um programa que recebe o salário de um colaborador e o reajuste segundo 
#        o seguinte critério, baseado no salário atual:
#    a) salários até R$ 280,00 (incluindo) : aumento de 20%
#    b) salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
#    c) salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
#    d) salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
    #    1) o salário antes do reajuste;
    #    2) o percentual de aumento aplicado;
    #    3) o valor do aumento;
    #    4) o novo salário, após o aumento.
# =============================================================================

salarioDoFuncionario = float(input("Digite o salario: "))

if salarioDoFuncionario <= 280.00:
    print("Salario antes do reajuste = R$ ", salarioDoFuncionario)
    print("Percentual aplicado 20% = R$ ", salarioDoFuncionario*0.20)
    print("Novo Salario apos aumento = R$ ", salarioDoFuncionario*1.20)
elif salarioDoFuncionario > 280.00 and salarioDoFuncionario <= 700.00:
    print("Salario antes do reajuste = R$ ", salarioDoFuncionario)
    print("Percentual aplicado 15% = R$ ", salarioDoFuncionario*0.15)
    print("Novo Salario apos aumento = R$ ", salarioDoFuncionario*1.15)
elif salarioDoFuncionario > 700.00 and salarioDoFuncionario < 1500:
    print("Salario antes do reajuste = R$ ", salarioDoFuncionario)
    print("Percentual aplicado 15% = R$ ", salarioDoFuncionario*0.10)
    print("Novo Salario apos aumento = R$ ", salarioDoFuncionario*1.10)
elif salarioDoFuncionario >= 1500.00:
    print("Salario antes do reajuste = R$ ", salarioDoFuncionario)
    print("Percentual aplicado 5% = R$ ", salarioDoFuncionario*0.05)
    print("Novo Salario apos aumento = R$ ", salarioDoFuncionario*1.05)

# =============================================================================
# 12 - QUESTÃO
# =============================================================================
"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, 
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% 
do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário 
Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas 
trabalhadas no mês.

Desconto do IR:
    
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. 
No exemplo o valor da hora é 5 e a quantidade de hora é 220.

        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00

"""

valorPorHora = float(input("digite o valor q vc ganha por HORA: "))
numeroHorasTrabalhadasPorMes = float(input("digite o numero de horas trabalhadas por mes: "))

#considerando o mês com 30 dias
#cosiderando o dia 24h e o mês 720h
salarioNoMes = numeroHorasTrabalhadasPorMes*valorPorHora

print("Salario no mês: ", salarioNoMes)






































































































































































