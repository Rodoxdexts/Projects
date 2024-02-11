
x = 1
while x == 1:
    input_operação = (input('Em qual operador deseja trabalhar?: \n| 1 = + | 2 = - | 3 = * | 4 = /\n| '))

    # Conversão do input_número_1 de string para número inteiro
    operação = int(input_operação)

    if operação == 1 or operação == 2 or operação == 3 or operação == 4:
        print('Correto!')
        # parar o loop (ou laço) while,(while - tradução - enquanto) enquanto x for igual a 1:, x recebe o valor de 0, antes 1, e o laço parar
        # mesma coisa se aplica nos próximos laços
        x = 0
    else:
        print('Errado!')


# Ou x=x+1 (x recebe o valor de x mais 1)
# Converte a o valor da variável x de 0 pra 1
# 👇mais simples
x = 1
while x == 1:
    input_número_1 = input('Número 1: ')

    if input_número_1.isnumeric():
        número_1 = int(input_número_1)
        x = 0
    else:
        print('Errado!')


# Recebe o valor do segundo número do usuário, em loop
x = 1
while x == 1:
    input_número_2 = input('Número 2: ')

    if input_número_2.isnumeric():
        # Conversão do input_número_2 de string para número inteiro
        número_2 = int(input_número_2)
        x = 0
    else:
        print('Errado!')


# Análise da operação e seus cálculos
# Adição
if operação == 1:
    print(f'{número_1} + {número_2} = {número_1 + número_2}')

# Subtração
elif operação == 2:
    print(f'{número_1} - {número_2} = {número_1 - número_2}')

# Multiplicação
elif operação == 3:
    print(f'{número_1} * {número_2} = {número_1 * número_2}')

# Divisão
elif operação == 4:
    print(f'{número_1} / {número_2} = {número_1 / número_2}')
