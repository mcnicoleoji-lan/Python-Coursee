# Input an integer value
n = int(input("Enter the number whose sum you want to find: "))

sum = 0

# Iterates from 1 to n (inclusive)
for i in range(1, n + 1):
    sum = sum + i

print("\nSum =", sum)
