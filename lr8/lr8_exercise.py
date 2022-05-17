# Define several variables containing lists of words, e.g., phrase1, phrase2, and so on.
# Join them together in various combinations (using the plus operator) to form whole sentences.
# What is the relationship between len(phrase1 + phrase2) and len(phrase1) + len(phrase2)?

phrase1 = ["word1", "word2", "word3", "word4", "word5"]
phrase2 = ["word5", "word6", "word7", "word8"]

phrase3 = phrase1 + phrase2
phrase4 = phrase1[:2] + phrase2[2:]

print(phrase3)
print(phrase4)


