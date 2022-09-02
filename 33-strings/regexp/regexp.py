import re

def find_big_words(text):
        m = re.findall("[A-Z]\w+", text)
        return m

print(find_big_words("Dies ist ein Text, den Python analysieren soll!"))

