word = input("Enter a word: ")
reverse_word = ""

for i in word:
    reverse_word = i + reverse_word
print((f"The reverse of the word {word} is: {reverse_word}"))