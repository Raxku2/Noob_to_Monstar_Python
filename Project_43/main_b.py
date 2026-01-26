def find_longest_sentence(text):
    sentences = text.split('.')
    longest = ""

    for s in sentences:
        s = s.strip()
        if len(s) > len(longest):
            longest = s

    return longest


# Main
user_input = input("Enter text with multiple sentences: ")

longest_sentence = find_longest_sentence(user_input)

print("Longest sentence is:")
print(longest_sentence)
