def desconto(preco, porcentagem):
    res = preco - (preco*(porcentagem/100))
    return res

def frete(preco, porcentagem):
    res = preco + (preco*(porcentagem/100))
    return res

def formatarMoeda(preco):
    return f'R$ {preco:.2f}'.replace('.', ',')

def total(preco, total):
    res = preco*total
    return res