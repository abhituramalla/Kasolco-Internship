def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
# Example usage
num = 6
print(f"Factorial of {num} is {factorial(num)}")
