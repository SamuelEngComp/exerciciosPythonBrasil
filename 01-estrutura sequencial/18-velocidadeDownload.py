"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) 
e a velocidade de um link de Internet (em Mbps), calcule e informe o 
tempo aproximado de download do arquivo usando este link (em minutos).
"""


"""
Velocidade em Mbps	Download de MB por segundo
    1	                   0.125
    2	                   0.25
   10	                   1.25
   20	                   2.5



100 Mbps  --->>> 12,5 MB/s

Mbps -> MB/s => 1Mbps/8 = MB/s
"""

tamanhoDoArquivoParaDownload = float(input("Digite o tamanho do arquivo em MB: "))
velocidadeDaInternet = float(input("Digite a velocidade da internet em Mbps: "))

megaBytesPorSegundo = velocidadeDaInternet / 8

tempoEmSegundos = tamanhoDoArquivoParaDownload / megaBytesPorSegundo

tempoEmMinutos = tempoEmSegundos / 60

