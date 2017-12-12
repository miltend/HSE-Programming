langLIST = []
language = "."

with open("lang.txt", encoding="utf-8") as f:
    lang = f.read()
lines = lang.splitlines()

while language != '':
    language = input('Введите язык:' )
    langLIST.append(language)

for bab in langLIST[:-1]:
    a = 0
    for line in lang:
        l1 = line.replace("   ","–")
        l1 = line.split("–")
        if bab in l1[0]:
            a = 1
            print(bab)
    if a == 0:
        print("Языка в списке нет")

# не работает :(
