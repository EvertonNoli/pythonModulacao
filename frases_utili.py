def contarPalavras(frase):

    palavras=frase.split()
    return len(palavras)

def contarLetras(frase):

    frase_sem_espaco = frase.replace(" ", "")
    return len(frase_sem_espaco)

def verificaPalindromo(frase):

    fraseLimpa = frase.replace(" ", "").lower()
    if fraseLimpa == fraseLimpa[::-1]:
        return 'Sim'
    else:
        return 'Não'