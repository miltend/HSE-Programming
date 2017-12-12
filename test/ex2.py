with open("lang.txt", encoding="utf-8") as f:
    lines = f.readlines()
num = 0    
for line in lines:
    a = line.find('Critically endangered')
    if a != -1:
        num += 1
print(num)
