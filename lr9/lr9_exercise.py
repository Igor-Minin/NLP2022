# Find all the four-letter words in the Chat Corpus (text5).
# With the help of a frequency distribution (FreqDist),
# show these words in decreasing order of frequency.

from nltk.book import *

fdist1 = FreqDist(text5)

fourLetterWord = [w[0] for w in fdist1.most_common() if len(w[0]) == 4]
print(fourLetterWord)
