import re

def words_from_text(fname):
    with open(fname, encoding='utf-8') as f:
        text = f.read()
    text = text.lower()
    return text

def findall(words):
    wordz = []
    result = re.findall('си[жд][еиуя][влмтшщ]?[аеиошь]?[аеийуя]?[геймхю]?[иоу]?', words)
    for word in result:
        if word not in wordz:
            wordz.append(word)
    print(wordz)
    return wordz

def main():
    findall(words_from_text('text.txt'))

main()
