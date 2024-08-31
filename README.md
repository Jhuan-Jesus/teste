Código questão 1


#simulando em python

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

    print(soma)

    #resultado = 91


Código Questão 2

def pertence_a_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

#entrada
num = int(input("Informe um número: "))

# Verificando se o numero pertence a sequência de Fibonacci
if pertence_a_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")



Código Questão 3 

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

#não consegui importar o arquivo json aqui no github


Código Questão 4

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

#calculando o total

valor_total = sp + rj + mg + es + outros

percentual_sp = (sp / valor_total) * 100
percentual_rj = (rj / valor_total) * 100
percentual_mg = (mg / valor_total) * 100
percentual_es = (es / valor_total) * 100
percentual_outros = (outros / valor_total) * 100

# resultado
print(f"O percentual de SP é {percentual_sp:.2f}%")
print(f"O percentual de RJ é {percentual_rj:.2f}%")
print(f"O percentual de MG é {percentual_mg:.2f}%")
print(f"O percentual de ES é {percentual_es:.2f}%")
print(f"O percentual de Outros é {percentual_outros:.2f}%")


Código Questão 5 

palavra = input("Digite uma palavra:")
palavra_invertida = ""

for letra in palavra:
    palavra_invertida = letra + palavra_invertida

print(palavra_invertida)

    

