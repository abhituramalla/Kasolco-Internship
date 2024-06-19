def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

# Example usage:
principal = 1000
rate = 5
time = 2
interest = simple_interest(principal, rate, time)
print(f"Simple Interest: {interest}")
