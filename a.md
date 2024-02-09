Para quebrar uma linha automaticamente ao digitar em Python, você pode usar o caractere de **quebra de linha**. Aqui estão algumas maneiras de fazer isso:

1. **Usando a sequência `\\n`**:
   - Basta adicionar `\\n` onde deseja que a quebra de linha ocorra. Por exemplo:
     ```python
     Nome = input("Digite o nome do cliente: ")
     DiaVencimento = input("Digite o dia de vencimento: ")
     MêsVencimento = input("Digite o mês de vencimento: ")
     ValorFatura = input("Digite o valor da fatura: ")
     print(f"Olá, {Nome}\\nA sua fatura com vencimento em {DiaVencimento} de {MêsVencimento} no valor de R${ValorFatura} está fechada.")
     ```
   - O `\\n` é convertido automaticamente para o caractere de quebra de linha usado em sistemas Unix.

2. **Usando o método `.format`**:
   - O método `.format` permite criar strings de saída de forma mais legível:
     ```python
     print("Olá {nome}\\nA sua fatura com vencimento em {vencimento} de {mesvencimento} no valor de R$ {valor:.2f} está fechada".format(nome=Nome, vencimento=DiaVencimento, mesvencimento=MêsVencimento, valor=float(ValorFatura)))
     ```

3. **Usando strings com prefixo `f`** (Python 3.6+):
   - Você pode formatar diretamente a partir das variáveis:
     ```python
     print(f"Olá, {Nome}\\nA sua fatura com vencimento em {DiaVencimento} de {MêsVencimento} no valor de R$ {ValorFatura} está fechada.")
     ```

Escolha a opção que melhor se adequa ao seu estilo de codificação! 🐍📝

Origem: conversa com o Bing, 08/02/2024
(1) python - Como quebrar a linha? - Stack Overflow em Português. https://pt.stackoverflow.com/questions/200818/como-quebrar-a-linha.
(2) Como faço para aplicar uma condição em uma linha que pule a próxima .... https://bing.com/search?q=como+se+faz+para+quando+digitar+automaticamente+pular+para+a+pr%c3%b3xima+linha+em+python.
(3) python - Como pular a linha na escrita dos arquivos? - Stack Overflow .... https://pt.stackoverflow.com/questions/179004/como-pular-a-linha-na-escrita-dos-arquivos.
(4) Como faço para aplicar uma condição em uma linha que pule a próxima .... https://pt.stackoverflow.com/questions/473043/como-fa%c3%a7o-para-aplicar-uma-condi%c3%a7%c3%a3o-em-uma-linha-que-pule-a-pr%c3%b3xima-iniciante.
(5) string - Como escrever múltiplas linhas em Python? - Stack Overflow em .... https://pt.stackoverflow.com/questions/80551/como-escrever-m%C3%BAltiplas-linhas-em-python.