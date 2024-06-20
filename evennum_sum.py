nums = list(map(int, input().split()))
sum_even = sum(n for n in nums if n % 2 == 0)
print(sum_even)
