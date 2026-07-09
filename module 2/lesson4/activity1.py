word = input("enter your word:")
char = input("Enter a character: ")

i = 0
count = 0


while i < len(word):
    if word[i] == char:
        count += 1
    i += 1

print(f"the total occurrence of '{char}' in '{word}' is: {count}")