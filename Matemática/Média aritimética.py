# incluir exibição de notas inseridas,normal ou lista/ou/listas
q_notas = int(input('Quantas notas você quer analizar: '))
notas = []
# x é a nota
for x in range(q_notas):
    # A expressão {x + 1} dentro da string de entrada do usuário é uma f-string (format string)
    # que substitui o valor de x + 1 na mensagem exibida para o usuário.
    # Isso significa que, para cada iteração do loop, a mensagem será algo como “Nota 1=”, “Nota 2=”, etc.
    nota = float(input(f'Nota {x +1}= '))
    notas.append(nota)

# para somar tudo sum(variedades de coisas)
op_notas = sum(notas)
resultado = op_notas / 2
print(f'Notas: {notas}')
print(resultado)
