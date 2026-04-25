# Entendendo o Código de Números Primos

## O que é Número Primo?

Um número primo é aquele que só pode ser dividido por 1 e por ele mesmo. Por exemplo: 2, 3, 5, 7, 11, 13... são primos. Já 4, 6, 8, 9, 10... não são porque podem ser divididos por outros números.

---

## As Funções do Programa

### 1. Função `eh_primo()` - Verifica se é primo

**O que faz:** Recebe um número e diz se é primo ou não.

**Como funciona:**

```
1. Se o número é menor que 2 → não é primo ❌
   (Números primos começam em 2)

2. Se o número é 2 → é primo ✓
   (2 é o único número par que é primo)

3. Se o número é par → não é primo ❌
   (Todos os pares maiores que 2 podem ser divididos por 2)

4. Agora testa números ímpares (3, 5, 7, 9, 11...)
   Para cada um, tenta dividir o número por eles
   Se conseguir dividir sem resto → não é primo ❌
   Se nenhum conseguir dividir → é primo ✓
```

**Truque inteligente:** Não testa até o final do número. Para testar 100, só precisa testar até 10 (porque √100 = 10). Se um número maior que 10 divide 100, um número menor também divide!

---

### 2. Função `encontrar_primos()` - Busca os primeiros primos

**O que faz:** Encontra uma quantidade específica de números primos.

**Como funciona:**

```
1. Começa com o número 2
2. Verifica se é primo usando a função anterior
3. Se for, adiciona à lista
4. Passa para o próximo número
5. Repete até conseguir a quantidade desejada
```

---

### 3. Função `exibir_verificacao()` - Mostra os resultados

**O que faz:** Exibe na tela se cada número é primo ou não.

**Exemplo de saída:**
```
  2 é primo
  3 é primo
  4 é não primo
  5 é primo
```

---

### 4. Função `main()` - Orquestra tudo

**O que faz:** Coordena o programa.

**Etapas:**

```
1. Cria uma lista com números para testar
2. Mostra se cada um é primo ou não
3. Procura os primeiros 10 números primos
4. Exibe o resultado: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## Como o Programa Funciona (Passo a Passo)

**Entrada:** Lista de números: 2, 3, 4, 5, 10, 17, 20, 29, 37, 100

**Processo:**
- Para cada número, chama `eh_primo()`
- A função verifica se é primo
- Mostra o resultado na tela

**Saída:**
```
Verificação de números primos:

  2 é primo
  3 é primo
  4 é não primo
  5 é primo
 10 é não primo
 17 é primo
 20 é não primo
 29 é primo
 37 é primo
100 é não primo

========================================

Os primeiros 10 números primos:
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

---

## Resumo Rápido

| Etapa | O que acontece |
|-------|--------------|
| Entrada | Recebe um número |
| Validação | Tira casos especiais (menores que 2, número 2, pares) |
| Teste | Tenta dividir por números até a raiz quadrada |
| Resultado | Retorna verdadeiro ou falso |
| Saída | Exibe se é primo ou não |

---

## Por que funciona bem?

✓ **Rápido:** Não testa até o final do número (usa truque da raiz quadrada)

✓ **Limpo:** Cada função tem uma responsabilidade

✓ **Fácil de usar:** Basta chamar `eh_primo(numero)` com o número desejado

✓ **Seguro:** Verifica se você passou um número de verdade
