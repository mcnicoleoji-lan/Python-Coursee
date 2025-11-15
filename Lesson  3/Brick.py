# Take user input
a = input("Enter a word: ")

# Program to check break keyword
for i in a:        # iterate through characters in the word
    if i == 'A':   # condition 1
        print("A is found")   # display result
        break                # break statement
else:
    # runs only if loop completes without break
    print("A not found")     # display result
