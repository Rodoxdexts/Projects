Em Python, o método `split()` é uma função útil para manipular strings. Ele permite dividir o conteúdo de uma variável de acordo com condições especificadas nos parâmetros da função ou com valores predefinidos por padrão. Vamos explorar como usar esse método e também como extrair dígitos de uma string para realizar operações.

## Dividindo uma string com `split()`

O método `split()` divide uma string em substrings com base em um caractere separador. A sintaxe é a seguinte:

```python
string.split(separador, maxsplit)
```

- `string`: é o nome da variável que servirá de base para a divisão.
- `separador`: indica o caractere usado como separador da string (por padrão, é o espaço).
- `maxsplit`: representa a quantidade máxima de divisões realizadas (por padrão, divide até o último caractere).

Exemplo:

```python
frase = "Python é incrível"
palavras = frase.split()  # Divide a frase em palavras
print(palavras)  # ['Python', 'é', 'incrível']
```

## Extraindo dígitos de uma string

Se você precisa extrair dígitos de uma string, pode usar o método `isdigit()`. Aqui está um exemplo de como fazer isso:

```python
texto = "96h11k"
apenas_digitos = []
for caractere in texto:
    if caractere.isdigit():
        apenas_digitos.append(caractere)
print(apenas_digitos)  # ['9', '6', '1', '1']
```

Agora você pode somar esses dígitos para obter o resultado desejado: \(9 + 6 + 1 + 1 = 17\).

Espero que isso ajude! Se tiver mais alguma dúvida, estou à disposição. 😊

Origem: conversa com o Bing, 09/02/2024
(1) Python split: separar strings em substrings e retornar listas!. https://blog.betrybe.com/python/python-split/.
(2) Como extrair dígitos de uma string? (extrair números de texto). https://horadecodar.com.br/como-extrair-digitos-de-uma-string-extrair-numeros-de-texto/.
(3) Dividir o inteiro em dígitos em Python | Delft Stack. https://bing.com/search?q=como+separar+strings+de+n%c3%bameros+para+operandos+em+python.
(4) python 3.x - Transformar string em operador - Stack Overflow em Português. https://pt.stackoverflow.com/questions/239800/transformar-string-em-operador.
(5) Como extrair dígitos de uma string em Python e somá-los entre si?. https://pt.stackoverflow.com/questions/42280/como-extrair-d%C3%ADgitos-de-uma-string-em-python-e-som%C3%A1-los-entre-si.