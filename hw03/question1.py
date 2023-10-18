

PUNCTUATION = ".,!?-:;\t\n()[]{}@#\\$%^*-_+= /'\"|~<>"

def sentences(prompt):
    user_input = input(prompt)
    cleaned_input = user_input.strip(PUNCTUATION)
    print(cleaned_input)
    words = cleaned_input.split()
    simplified_words = []
    for word in words:
        word = word.translate(str.maketrans('', '', PUNCTUATION))
        if word.isalpha():
            simplified_words.append(word.upper())
    return simplified_words, len(simplified_words)

if __name__ == '__main__':
    result = sentences("Please enter a sentence:\n")
    print(result)
