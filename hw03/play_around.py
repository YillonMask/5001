
PUNCTUATION = ".,!?-:;\t\n()[]{}@#\\$%^*-_+= /'\"|~<>"

sentence = "..Time flies, like an arrow!!"

# Remove punctuation using replace()
cleaned_sentence = sentence
for char in PUNCTUATION:
    cleaned_sentence = cleaned_sentence.replace(char, " ")
print(cleaned_sentence)
# Split the cleaned sentence into words
words = cleaned_sentence.split()

print(words)
# Output: ['Hello', 'how', 'are', 'you']

