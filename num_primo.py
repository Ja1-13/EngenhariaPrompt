def is_prime(number: int) -> bool:
    """Retorna True se o número for primo e False caso contrário."""
    if number <= 1:
        return False
    if number <= 3:
        return True
    if _is_multiple_of_two_or_three(number):
        return False
    return not _has_divisor_in_candidate_range(number)


def _is_multiple_of_two_or_three(number: int) -> bool:
    return number % 2 == 0 or number % 3 == 0


def _has_divisor_in_candidate_range(number: int) -> bool:
    """Verifica divisores potenciais do tipo 6k-1 e 6k+1."""
    candidate = 5
    while candidate * candidate <= number:
        if number % candidate == 0 or number % (candidate + 2) == 0:
            return True
        candidate += 6
    return False


def run_tests() -> None:
    test_cases = [
        (2, True),
        (3, True),
        (4, False),
        (17, True),
        (18, False),
        (19, True),
        (1, False),
        (0, False),
        (-5, False),
        (97, True),
        (100, False),
    ]

    all_passed = True
    for value, expected in test_cases:
        result = is_prime(value)
        if result != expected:
            print(f"Falha: {value} -> resultado={result}, esperado={expected}")
            all_passed = False

    if all_passed:
        print("Todos os testes passaram com sucesso.")


def main() -> None:
    run_tests()


if __name__ == "__main__":
    main()
