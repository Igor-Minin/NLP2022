import nltk

from nltk.book import *

# Your Turn: Try searching for other words; to save re-typing,
# you might be able to use up-arrow, Ctrl-up-arrow or Alt-p
# to access the previous command and modify the word being searched.
# You can also try searches on some of the other texts we have included.
# For example, search Sense and Sensibility for the word affection,
# using text2.concordance("affection"). Search the book of Genesis
# to find out how long some people lived, using text3.concordance("lived").
# You could look at text4, the Inaugural Address Corpus, to see examples
# of English going back to 1789, and search for words like nation, terror,
# god to see how these words have been used differently over time.
# We've also included text5, the NPS Chat Corpus: search this for
# unconventional words like im, ur, lol. (Note that this corpus is uncensored!)

text2.concordance("affection")
text3.concordance("lived")
text4.concordance("god")
text5.concordance("lmao")

print()

# Your Turn: Pick another pair of words and compare their usage in two
# different texts, using the similar() and common_contexts() functions.
text5.similar("lol")
text5.common_contexts(["lol", "lmao"])

print()

# Your Turn: How many times does the word lol appear in text5?
# How much is this as a percentage of the total number of words in this text?
print(text5.count("lol"))
print(100 * text5.count('lol') / len(text5))

print()

# Your Turn: Make up a few sentences of your own, by typing a name,
# equals sign, and a list of words, like this:
# ex1 = ['Monty', 'Python', 'and', 'the', 'Holy', 'Grail'].
# Repeat some of the other Python operations we saw earlier in 1,
# e.g., sorted(ex1), len(set(ex1)), ex1.count('the').

sentence = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. In dui dolor, varius vitae lectus nec, " \
           "accumsan lacinia ipsum. Nunc ac justo magna. Nulla finibus, nisl quis condimentum laoreet, " \
           "eros ex vulputate magna, ut facilisis massa odio ut leo. Suspendisse potenti. Mauris fringilla sapien sed " \
           "euismod faucibus. In orci erat, maximus ut elementum a, pretium sed neque. Praesent laoreet ac arcu eu " \
           "sodales. Praesent nec suscipit arcu. Donec dignissim lacinia dui et maximus. Morbi vel velit lacus. Proin " \
           "tristique a lectus sit amet elementum. Proin sed hendrerit ipsum, imperdiet dapibus est. Pellentesque " \
           "tristique massa nec est volutpat sagittis. Morbi pellentesque ipsum nec leo iaculis egestas vitae a velit. "


words = ["ut", "faucibus", "sit"]

print("Number of words in sentence: ", len(sentence))
print("Number of unique words in sentence: ", len(set(sentence)))
for word in words:
    print(word, "is repeated", sentence.count(word), "in sentence")

print()
# Your Turn: Take a few minutes to define a sentence of your own and modify
# individual words and groups of words (slices) using the same methods used earlier.
# Check your understanding by trying the exercises on lists at the end of this chapter.
sentence1 = nltk.word_tokenize("Lorem ipsum dolor sit amet, consectetur adipiscing elit")
sentence1[0] = "*Changed*"
sentence1[5:8] = ""
print(sentence1)
