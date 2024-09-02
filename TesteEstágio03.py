import json

def calcular_faturamento(faturamento_diario):
    dias_com_faturamento = [valor for valor in faturamento_diario if valor > 0]
    
    if not dias_com_faturamento:
        return "Não há dias com faturamento."

    menor_faturamento = min(dias_com_faturamento)
    maior_faturamento = max(dias_com_faturamento)

    media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

    dias_acima_media = sum(1 for valor in dias_com_faturamento if valor > media_mensal)

    return {
        'menor_faturamento': menor_faturamento,
        'maior_faturamento': maior_faturamento,
        'dias_acima_media': dias_acima_media
    }

with open('TesteEstagio03.json', 'r') as file:
    dados = json.load(file)

faturamento_diario = dados['faturamento_diario']

resultados = calcular_faturamento(faturamento_diario)
print(f"Menor faturamento: {resultados['menor_faturamento']}")
print(f"Maior faturamento: {resultados['maior_faturamento']}")
print(f"Número de dias acima da média: {resultados['dias_acima_media']}")
