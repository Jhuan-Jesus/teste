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