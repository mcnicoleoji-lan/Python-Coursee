class FlashingTheCards:
    def __init__(self, word, meaning):
        self.words = word
        self.meaning = meaning

    def __str__(self):
        return self.words + ": (" + self.meaning + ")"

flash = []
print("Welcome to Flashing the Cards!")

while True:
    word = input("Enter the name you want to add to the flashcards: ")
    meaning = input("Enter the meaning of the word: ")
    flash.append(FlashingTheCards(word, meaning))
    option = input("Do you want to add more flashcards? (yes/no): ")
    if option.lower() != 'yes':
        break

print("\nYour Flashcards:")
for card in flash:
    print(card)