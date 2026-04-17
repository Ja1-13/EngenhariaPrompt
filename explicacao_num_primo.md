# Explicação do código em `num_primo.py`

## Objetivo

O arquivo `num_primo.py` define uma função para verificar se um número inteiro é primo e inclui um conjunto de testes automáticos para validar a lógica.

## Função principal: `is_prime(number)`

- Primeiro, elimina casos triviais:
  - números menores ou iguais a 1 não são primos;
  - 2 e 3 são tratados como primos diretamente.
- Depois, verifica se o número é múltiplo de 2 ou 3. Se for, retorna `False`.
- Caso contrário, delega a verificação de possíveis divisores maiores para a função auxiliar `_has_divisor_in_candidate_range()`.

## Funções auxiliares

### `_is_multiple_of_two_or_three(number)`

- Retorna `True` se o número for divisível por 2 ou por 3.
- Essa verificação rápida descarta muitos casos antes de iniciar a busca mais cara por divisores.

### `_has_divisor_in_candidate_range(number)`

- Utiliza a técnica de testar apenas os números do tipo `6k - 1` e `6k + 1`.
- Começa em 5 e, a cada passo, testa o par `candidate` e `candidate + 2`.
- Para verificar primalidade, não é preciso testar todos os números até `n`, apenas até `sqrt(n)`.
- Se encontrar qualquer divisor, retorna `True`; caso contrário, retorna `False`.

## Bloco de execução principal

- A função `run_tests()` define uma lista de casos de teste com valores e resultados esperados.
- Cada caso é executado com `is_prime()`.
- Se todos os testes passarem, o script imprime:

```
Todos os testes passaram com sucesso.
```

- A função `main()` chama `run_tests()` quando o arquivo é executado diretamente.

## Por que essa versão é mais limpa

- Organização em funções pequenas e nomeadas deixa o código mais fácil de entender.
- O uso de nomes claros (`number`, `test_cases`, `all_passed`) melhora a legibilidade.
- O bloco `main()` separa a lógica de teste da implementação da verificação de primalidade.
- A técnica `6k ± 1` torna a verificação eficiente sem perder clareza.
