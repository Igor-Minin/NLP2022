import re

import nltk
from urllib import request

url = "https://www.gutenberg.org/files/1661/1661-h/1661-h.htm"
response = request.urlopen(url)
raw = response.read().decode('utf8')

print("Number of words in text:", len(nltk.word_tokenize(raw)))
print("Number of \'the of\' int text:", raw.count("the of"))


# Your Turn: Create a file called document.txt using a text editor,
# and type in a few lines of text, and save it as plain text.
# If you are using IDLE, select the New Window command in the File menu,
# typing the required text into this window, and then saving the file as
# document.txt inside the directory that IDLE offers in the pop-up dialogue box.
# Next, in the Python interpreter, open the file using f = open('document.txt'),
# then inspect its contents using print(f.read()).

f = open("document.txt")
print(f.read())


# Your Turn: Look for some "finger-twisters", by searching for words that only
# use part of the number-pad. For example «^[ghijklmno]+$», or more concisely,
# «^[g-o]+$», will match words that only use keys 4, 5, 6 in the center row,
# and «^[a-fj-o]+$» will match words that use keys 2, 3, 5, 6 in the top-right corner. What do - and + mean?
str = "go"

print(re.search("^[g-o]+$", str))


# Your Turn: In the W3C Date Time Format, dates are represented like this:
# 2009-12-31. Replace the ? in the following Python code with a regular expression,
# in order to convert the string '2009-12-31' to a list of integers [2009, 12, 31]
date = '2009-12-31'
dateList = date.split("-")
print(list(map(int, dateList)))
