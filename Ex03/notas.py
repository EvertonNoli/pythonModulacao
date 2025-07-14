def calcularMedia(lista_notas):
    res = sum(lista_notas)/len(lista_notas)
    return res

def mostrarResultado(media):
    if media >=7:
        return 'Aprovado'
    elif media>=5 and media <7:
        return 'Recuperação'
    else:
        return 'Reprovado'

def formataBoletim(nome, nota, media, situacao, ):

    return (
        f'Aluno: {nome}\n'
        f'Nota: {nota}\n'
        f'Media: {media:.2f}\n'
        f'Situação: {situacao}\n'

    )