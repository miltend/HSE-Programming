import re
 
def readfile(name):
    with open(name+".html", "r", encoding="utf-8") as f:
        return f.read()
 
def writefile(text,name):
    with open(name+".txt", "w", encoding="utf-8") as f:
        f.write(text)
    if not f.writable:
        print("Unable to get access to the end file.")
 
def search(text):
    i = 1
    text = text.split("\n")
    for line in text:
        if re.search("ISO 639-3", line):
            tmp = text[i]
            tmp = re.findall(">[a-z][a-z][a-z]<", tmp)
            return str(tmp)
        i += 1
 
writefile(search(readfile(input("Start file: "))), input("End file: "))
