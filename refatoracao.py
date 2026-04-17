def calculate_statistics(numbers):
    """
    Calcula estatísticas básicas de uma lista de números.
    
    Args:
        numbers (list): Lista de números para análise.
    
    Returns:
        tuple: (total, média, máximo, mínimo)
    """
    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    
    return total, average, maximum, minimum


# Dados para análise
data = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]

# Calcula as estatísticas
total, average, maximum, minimum = calculate_statistics(data)

# Exibe os resultados
print("Total:", total)
print("Média:", average)
print("Maior:", maximum)
print("Menor:", minimum)