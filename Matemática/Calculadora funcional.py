
# Área de loop while
# Variável que 
# valor = 0
# Enquanto while é menor que 10
# while valor < 10:
# pegar uma string e converter em variável, e realizar o cálculo


números = input('Expressão aritmética: ')


resultado = eval(números)

print(resultado)


# mais seguro, ast.literal_eval quando eu precisar disso talvez eu coloque
# número = input('Conta matemática: ')
# valores = []

# for dígito in número:
#     if dígito.isdigit():
#         valores.append(int(dígito))

# operadores = [+ - * /]

# for operador in operadores:
#     if número is operador:
#         operadores.append(operador)

# print(valores)


# Conversão
# con = float(n1)
# print(f'Resultado = {n1}')


# # Leitura do primeiro valor
# n = float(input('Insira o primeiro valor_: '))
# # Seleção de operando
# op = input('+ (adição), - (subtração), * (multiplicação), / (divisão)')
# # Seleção de segundo operando
# n2 = float(input('Insira o segundo valor_: '))
# # Área dos se op igual a 'algo'
# if op == '+':
#     print(f'{n + n2}')
# if op == '-':
#     print(f'{n - n2}')
# if op == '*':
#     print(f'{n * n2}')
# if op == '/':
#     print(f'{n / n2}')
# # Adicionar valor à variável 'valor', se a variável valor chegar a 10 o programa termina por causa do laço while
# valor + 1
