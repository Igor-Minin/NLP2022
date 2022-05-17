# Write a utility function that takes a URL as its argument,
# and returns the contents of the URL, with all HTML
# markup removed. Use from urllib import request and then
# request.urlopen('http://nltk.org/').read().decode('utf8')
# to access the contents of the URL.
import re
from urllib import request

url = "http://nltk.org/"


def clearHTML(URL):
    page = request.urlopen(URL).read().decode('utf8')
    return re.sub("<[\w =\"/:+-._#]+>", "", page)


print(clearHTML(url))
