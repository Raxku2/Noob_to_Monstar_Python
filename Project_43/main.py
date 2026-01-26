# Take input from user
text = input("Enter a text: ")

vowels = []
consonants = []

# Loop through each character
for ch in text:
    # Check only alphabets
    if ch.isalpha():
        if ch.lower() in ['a', 'e', 'i', 'o', 'u']:
            vowels.append(ch)
        else:
            consonants.append(ch)

# Print results
print("Vowels:", vowels)
print("Consonants:", consonants)
