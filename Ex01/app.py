import preco

valor = float(input('Digite o valor:$'))
taxaDesc = float(input('Digite a taxa de desconto:%'))
taxaJur = float(input('Digite a taxa de juros:%'))

print(f'A metade do valor digitado é {preco.metade(valor):.2f}')
print(f'O dobro do valor digitado é {preco.dobro(valor):.2f}')
print(f'Com desconto de {taxaDesc}% o valor vai para {preco.desconto(valor, taxaDesc):.2f}')
print(f'Com juros de {taxaJur}% o valor vai para {preco.juros(valor, taxaJur):.2f}')
