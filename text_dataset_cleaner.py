# Take text input from the user
text = input("Enter text: ")

# Convert text to lowercase
text = text.lower()

# Remove punctuation marks
punctuations = ".,!?:;"
for p in punctuations:
    text = text.replace(p, "")

# Split text into words
words = text.split()  # <-- words stored in a list

# Store word frequency in a dictionary
word_frequency = {}
for word in words:
    word_frequency[word] = word_frequency.get(word, 0) + 1

# Print results
print("\nCleaned text:")
print(text)

print("\nWords list:")
print(words)  # <-- explicitly show the list of words

print("\nWord frequency result:")
print(word_frequency)
