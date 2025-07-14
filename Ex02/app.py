import preco

valor = float(input('Digite o valor do produto:'))
quantidade = int(input('Digite a quantidade:'))
taxaDesc = float(input('Digite a taxa de desconto:%'))
taxaFrete = float(input('Digite a taxa de frete:%'))
precoDesc = preco.desconto(valor, taxaDesc)
precoFrete = preco.frete(valor, taxaFrete)
precoTotal = preco.total(valor, quantidade)

print(f'Valor original: {preco.formatarMoeda(valor)}')
print(f'Valor total: {preco.formatarMoeda(precoTotal)}')
print(f'Valor com {taxaDesc}% de desconto:R${precoDesc:.2f}')
print(f'Valor com {taxaFrete}% de frete:R${precoFrete:.2f}')