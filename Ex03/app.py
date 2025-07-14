import notas

aluno = []

while True:

    nome = str(input('Nome: '))
    nota1 = float(input('Primeira nota: '))
    nota2 = float(input('Segunda nota: '))
    nota3 = float(input('Terceira nota: '))

    lista_notas = [nota1,nota2, nota3]
    media = notas.calcularMedia(lista_notas)
    situacao = notas.mostrarResultado(media)
    boletim = notas.formataBoletim(nome, lista_notas, media, situacao)
    aluno.append(boletim)

    opc = ' '
    while opc not in 'SN':
        opc = str(input('Deseja realizar outro cadastro?[S/N]')).upper().strip()
    if opc == 'N':
        break

print('\n=== RELATÓRIO FINAL ===')
for a in aluno:
    print(a)