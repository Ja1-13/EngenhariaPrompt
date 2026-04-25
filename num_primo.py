"""Módulo para verificação e busca de números primos."""


def eh_primo(numero: int) -> bool:
    """
    Verifica se um número é primo.

    Args:
        numero: O número a ser verificado.

    Returns:
        True se o número é primo, False caso contrário.

    Raises:
        TypeError: Se o número não for inteiro.
    """
    if not isinstance(numero, int):
        raise TypeError(f"Esperado int, recebido {type(numero).__name__}")

    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False

    divisor = 3
    while divisor * divisor <= numero:
        if numero % divisor == 0:
            return False
        divisor += 2

    return True


def encontrar_primos(quantidade: int) -> list[int]:
    """
    Encontra os primeiros N números primos.

    Args:
        quantidade: Quantidade de primos a encontrar.

    Returns:
        Lista com os primeiros N números primos.

    Raises:
        ValueError: Se quantidade for menor que 1.
    """
    if quantidade < 1:
        raise ValueError("Quantidade deve ser maior que 0")

    primos = []
    numero = 2

    while len(primos) < quantidade:
        if eh_primo(numero):
            primos.append(numero)
        numero += 1

    return primos


def exibir_verificacao(numeros: list[int]) -> None:
    """
    Exibe se cada número na lista é primo ou não.

    Args:
        numeros: Lista de números a verificar.
    """
    print("Verificação de números primos:\n")
    for num in numeros:
        status = "primo" if eh_primo(num) else "não primo"
        print(f"{num:>3} é {status}")


def main() -> None:
    """Função principal - executa exemplos de uso."""
    numeros_teste = [2, 3, 4, 5, 10, 17, 20, 29, 37, 100]
    exibir_verificacao(numeros_teste)

    print("\n" + "=" * 40)
    print("\nOs primeiros 10 números primos:")
    primos = encontrar_primos(10)
    print(primos)


if __name__ == "__main__":
    main()
