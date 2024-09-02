faturamentodist = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53
}

totalFaturamento = sum(faturamentodist.values())

percentuais = {estado: (valor / totalFaturamento) * 100 for estado, valor in faturamentodist.items()}

for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual:.2f}%')
    