def calculate_sum(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    return total / len(numbers)  # Деление на len, возможна ошибка при пустом списке

nums = [10, 20, 30]
print(calculate_sum(nums))
