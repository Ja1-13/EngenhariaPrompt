def calculate_statistics(numbers):
    """Return total, average, maximum and minimum for a sequence of numbers."""
    if not numbers:
        raise ValueError("A lista de números não pode estar vazia.")

    total = sum(numbers)
    average = total / len(numbers)
    maximum = max(numbers)
    minimum = min(numbers)

    return total, average, maximum, minimum

if __name__ == "__main__":
    values = [23, 7, 45, 2, 67, 12, 89, 34, 56, 11]
    total, average, maximum, minimum = calculate_statistics(values)

    print("total:", total)
    print("média:", average)
    print("maior:", maximum)
    print("menor:", minimum)