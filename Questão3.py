import json

# Abrindo o arquivo 
with open('project.json', 'r') as f:
    project = json.load(f)

# dias com faturamento positivo
faturamento_filtrado = [dia['valor'] for dia in project if dia['valor'] > 0]

# menor valor de faturamento
menor_faturamento = min(faturamento_filtrado)

# maior valor de faturamento
maior_faturamento = max(faturamento_filtrado)

# Calculando a media do faturamento
media_mensal = sum(faturamento_filtrado) / len(faturamento_filtrado)

# dias de faturamento acima da média
dias_acima_da_media = sum(1 for valor in faturamento_filtrado if valor > media_mensal)

# resultados
print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média: {dias_acima_da_media}")
