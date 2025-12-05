valid = False

while not valid:
    try:
        n = int(input("Enter a number: "))
        # enter an even number
        while n % 2 == 0:
            print("bye")
            valid = True
