def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True  # 2 is prime
    if num % 2 == 0:
        return False  # other even numbers are not prime
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Example usage:
number = 23
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")
