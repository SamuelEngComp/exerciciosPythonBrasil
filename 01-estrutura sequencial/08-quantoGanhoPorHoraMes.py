# =============================================================================
# Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês
# =============================================================================

valorPorHora = float(input("digite o valor q vc ganha por HORA: "))
numeroHorasTrabalhadasPorMes = float(input("digite o numero de horas trabalhadas por mes: "))

#considerando o mês com 30 dias
#cosiderando o dia 24h e o mês 720h
salarioNoMes = numeroHorasTrabalhadasPorMes*valorPorHora

print("Salario no mês: ", salarioNoMes)