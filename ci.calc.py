def compound_interest(principal, rate, time):
    amount = principal * (pow((1 + rate / 100), time))
    return amount - principal

# Example usage:
principal = 1000
rate = 5
time = 2
interest = compound_interest(principal, rate, time)
print(f"Compound Interest: {interest}")
