n = int(input("Enter a number: "))
sum = 0
i = 1
while i <= n:
    sum=i+sum
    print(f"sum after adding {i}: {sum}")
    i = i + 1