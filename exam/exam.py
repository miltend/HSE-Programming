import re
import os

def readfile(fname):
    with open("news/" + fname, "r", encoding="utf-8") as f:
        text =f.read()
    title = re.search('<title>([^<]+)</title>', text)
    text = re.sub("(\<(/?[^>]+)>)", "", text)
    text = text.replace("`", "")
    with open(fname[:fname.find('.')] + ".txt", "w", encoding="cp1251") as f:
        f.write(text)
        
    if not f.writable:
        print("Unable to get access to the end file.")

for fname in os.listdir('news'):
    readfile(fname)
