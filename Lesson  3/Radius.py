# Calculating circumference of a circle
r = float(input("Enter radius: "))

# definition of function
def circle_circumference(r):
    return 2 * 3.14 * r

print(circle_circumference(9))  # Here you pass the value of r, you have to pass a number


def weather_condition():
    print("weather is pleasant in", spring)
    print("weather is same in", autumn)


spring = "autumn"
autumn = "winter"
weather_condition()

def add(P, Q):
    return P + Q

def subtract(P, Q):
    return P - Q

def multiply(P, Q):
    return P * Q

def divide(P, Q):
    return P / Q
# Now we will take inputs from the user
print("Please select operation.")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. Divide")

choice = input("Please enter choice (a/b/c/d): ")

num_1 = int(input("Please enter the first number: "))
num_2 = int(input("Please enter the second number: "))
if choice == 'a':
    print(num_1, "+", num_2, "=", add(num_1, num_2))

elif choice == 'b':
    print(num_1, "-", num_2, "=", subtract(num_1, num_2))

elif choice == 'c':
    print(num_1, "*", num_2, "=", multiply(num_1, num_2))

elif choice == 'd':
    print(num_1, "/", num_2, "=", divide(num_1, num_2))

else:
    print("This is an invalid input")