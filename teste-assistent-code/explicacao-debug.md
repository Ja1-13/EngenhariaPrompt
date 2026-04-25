# Explicação do debug em `debug.py`

Este arquivo descreve, de forma didática, as etapas solicitadas: identificação dos erros, explicação da causa e proposta de correção.

## 1. Erros identificados

### 1.1. Erro de sintaxe no `input`
No trecho:

```python
item1 = float(input(Preço do item 1? ))
```

Faltam aspas ao redor do texto que deve ser mostrado ao usuário. O Python interpreta `Preço` como um nome de variável, o que gera um erro de sintaxe.

### 1.2. Conversão de tipo ausente para o cupom de desconto
No trecho:

```python
desconto_cupom = (input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)
```

A função `input()` retorna texto (`str`). Em seguida, o código tenta dividir esse texto por `100` e comparar com `0`. Isso causa erro de tipo ou comportamento inválido porque `desconto_cupom` não foi convertido para número.

### 1.3. Impressão incorreta do valor de Item 2
No trecho:

```python
print(" Item 2:        R$ {total_item2:.2f}")
```

Foi escrita uma string regular em vez de uma `f-string`. Assim, o Python imprime exatamente `{total_item2:.2f}` em vez do valor calculado.

### 1.4. Indentação incorreta no `if`
No trecho:

```python
if desconto_cupom > 0: 
print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")
```

A linha dentro do `if` não está indentada, causando `IndentationError` e impedindo a execução correta do bloco condicional.

## 2. Causa de cada erro

- `item1 = float(input(Preço do item 1? ))`: falta de aspas transforma a mensagem em código inválido.
- `input()` sem conversão para número: o valor digitado pelo usuário permanece como string.
- `print(" Item 2:        R$ {total_item2:.2f}")`: sem `f`, não há interpolação de variáveis.
- falta de indentação no bloco `if`: o Python exige blocos corretamente recuados.

## 3. Proposta de correção

A seguir, a versão corrigida do código com as mudanças necessárias:

```python
# ENTRADA DE DADOS
cliente = input("Qual é seu nome? ")

qtd1 = int(input("Quantidade do item 1: "))
item1 = float(input("Preço do item 1? "))

qtd2 = int(input("Quantidade do item 2: "))
item2 = float(input("Preço do item 2? "))

qtd3 = int(input("Quantidade do item 3: "))
item3 = float(input("Preço do item 3? "))

# CÁLCULOS DOS ITENS
total_item1 = qtd1 * item1
total_item2 = qtd2 * item2
total_item3 = qtd3 * item3

subtotal = total_item1 + total_item2 + total_item3
imposto = subtotal * 0.10

# DESCONTO
desconto_cupom = float(input("Você tem um cupom de desconto? (Digite o percentual ou 0): "))
desconto = subtotal * (desconto_cupom / 100)

# TOTAL FINAL
total = subtotal + imposto - desconto

# EXIBIÇÃO
linha = "=" * 31
separador = "-" * 31

print(linha)
print(f" Cliente: {cliente}")
print(linha)
print(f" Item 1:        R$ {total_item1:.2f}")
print(f" Item 2:        R$ {total_item2:.2f}")
print(f" Item 3:        R$ {total_item3:.2f}")
print(separador)
print(f" Subtotal:      R$ {subtotal:.2f}")
print(f" Imposto (10%): R$ {imposto:.2f}")

if desconto_cupom > 0:
    print(f" Desconto ({desconto_cupom:.0f}%): -R$ {desconto:.2f}")

print(linha)
print(f" TOTAL:         R$ {total:.2f}")
print(linha)
```

## 4. Observações didáticas

- Sempre verifique se as strings de `input()` estão entre aspas.
- Converta imediatamente o valor de `input()` quando precisar fazer cálculos.
- Use `f"..."` para inserir valores de variáveis dentro de uma string.
- Em Python, blocos condicionais precisam de indentação correta para funcionar.

> Dica: se quiser, também é possível adicionar validação extra para garantir que o usuário não digite texto inválido ao pedir números.