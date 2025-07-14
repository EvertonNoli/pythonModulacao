def metade(valor):
    res = valor/2
    return res

def dobro(valor):
    res = valor*2
    return res

def desconto(valor, taxa):
    res = valor - (valor*(taxa/100))
    return res

def juros(valor, taxa):
    res = valor + (valor*(taxa/100))
    return res