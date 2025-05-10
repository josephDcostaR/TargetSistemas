# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def analisar_faturamento(arq_path):
    with open(arq_path, 'r') as file:
        dados = json.load(file)

    dias_uteis = [d for d in dados if d["valor"] > 0]

    if not dias_uteis:
        print("Não há dados de faturamento úteis para análise.")
        return

    valores = [d["valor"] for d in dias_uteis]
    media = sum(valores) / len(valores)

    menor_dia = min(dias_uteis, key=lambda x: x["valor"])
    maior_dia = max(dias_uteis, key=lambda x: x["valor"])
    acima_media = [d for d in dias_uteis if d["valor"] > media]

    print(f"Dia com o menor faturamento: {menor_dia['dia']} - R$ {menor_dia['valor']:.2f}")
    print(f"Dia com o maior faturamento: {maior_dia['dia']} - R$ {maior_dia['valor']:.2f}")
    print(f"Dias com faturamento acima da média ({media:.2f}): {len(acima_media)}")

# chamada da função
if __name__ == "__main__":
    analisar_faturamento("Atv3-Faturamento.json")
