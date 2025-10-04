# Take marks as input from user
print("Enter Marks Obtained in 4 Subjects: ")
math = int(input("Maths: "))
english = int(input("English: "))
science = int(input("Science: "))
history = int(input("History: "))

# Calculate the total and percentage
total = math + english + science + hindi
print("Total marks in Math, English, Science, and History:", total)

# Assuming each subject is out of 100
perc = (total / 400) * 100

# Display percentage
print("Percentage Mark =", perc, "%")