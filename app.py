import frases_utili

frase = str(input('Digite uma frase: '))

total_palavras = frases_utili.contarPalavras(frase)
total_letras = frases_utili.contarLetras(frase)
eh_palindromo = frases_utili.verificaPalindromo(frase)

print(f'A frase analisada foi: {frase}')
print(f'A frase tem {total_palavras} palavra(s)')
print(f'A frase tem {total_letras} letra(s)')
print(f'É um palíndromo? {eh_palindromo}')