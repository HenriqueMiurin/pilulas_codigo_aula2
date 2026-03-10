import math
assinantes = int(input('Digite a quantidade de assinantes: '))
mensalidade = float(input('Digite o valor da mensalidade: '))
taxa = float(input('Digite a taxa de crecimento mensal %: '))/100
meses = int(input('Digite a quantidade de meses da projeção: '))
#processamento
assinantes_finais = assinantes * math.pow((1 + taxa), meses)
receita_final = assinantes_finais * mensalidade 
#saida
print(f"Assinantes estimados: {assinantes_finais:.0f}")
print(f"Receita estimada: {receita_final:.2f}")