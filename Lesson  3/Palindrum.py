# take input from user
num = int(input("Enter a number: "))
rev = 0

# store original number for comparison
temp = num

# checking each digit to reverse the number
while temp > 0:
    rem = temp % 10
    rev = (rev * 10) + rem
    temp = temp // 10

# display the result
if rev == num:
    print("\nIt is a Palindrome Number")
else:
    print("\nIt is not a Palindrome Number")
