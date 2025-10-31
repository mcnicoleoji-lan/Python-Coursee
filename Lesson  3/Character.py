# Take input of a word
string = input("Please enter your own word: ")

# Take input of a character
char = input("Please enter your own character: ")

i = 0
count = 0

# Loop will find the occurrence of character
while i < len(string):  # string operation
    if string[i] == char:  # condition 1
        count = count + 1
    i = i + 1

# Display the result
print("The total number of times '", char, "' has occurred =", count)
print("The total Number of Times", char, "has Occurred =", count)
