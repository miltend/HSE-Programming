list1 = []
with open("lang.txt", encoding="utf-8") as f:
    lang = f.read()
lines = lang.splitlines()
for line in lines:
    if len(line) > 35:
        list1.append(line)
for line in list1:
    print(line)
