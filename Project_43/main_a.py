def remove_and_find_duplicates(text):
    unique_chars = ""
    duplicate_chars = ""

    for ch in text:
        if ch not in unique_chars:
            unique_chars += ch
        else:
            if ch not in duplicate_chars:
                duplicate_chars += ch

    return unique_chars, duplicate_chars


# Main
user_input = input("Enter a text: ")

unique, duplicates = remove_and_find_duplicates(user_input)

print("Text after removing duplicates:", unique)
print("Duplicate characters:", duplicates)
