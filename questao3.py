import xml.etree.ElementTree as ET

tree = ET.parse('dados.xml')
root = tree.getroot()

faturamento = []
for child in root:
    valor = float(child.find('valor').text)
    faturamento.append(valor)

menor_valor = min(faturamento)
maior_valor = max(faturamento)

dias_com_faturamento = []
for valor in faturamento:
    if valor > 0:
        dias_com_faturamento.append(valor)

media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_da_media = 0
for valor in faturamento:
    if valor > media_mensal:
        dias_acima_da_media += 1

print("Menor valor de faturamento do mês: R$ {:.2f}".format(menor_valor))
print("Maior valor de faturamento do mês: R$ {:.2f}".format(maior_valor))
print("Número de dias com faturamento acima da média mensal: {}".format(dias_acima_da_media))