# Taking total amount as input from user
amount = int(input("Please Enter Amount to Withdraw: "))

# Calculating notes of different denominations
note_100 = amount // 100
note_50 = (amount % 100) // 50
note_10 = (amount % 50) // 10
remaining = amount % 10   # leftover if not multiple of 10

# Display results
print("Notes of 100 naira:", note_100)
print("Notes of 50 naira :", note_50)
print("Notes of 10 naira :", note_10)

if remaining != 0:
    print("Remaining amount that cannot be withdrawn:", remaining)