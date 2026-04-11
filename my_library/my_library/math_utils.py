def calculate_mean(numbers): 
    return sum(numbers) / len(numbers) 
 
def factorial(n): 
    if n < 0: 
        raise ValueError("Факториал определён только для неотрицательных чисел.") 
    if n == 0: 
        return 1 
    return n * factorial(n - 1) 
