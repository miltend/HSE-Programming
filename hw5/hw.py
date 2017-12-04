words = []
for i in range(8):
    words.append(input("Введите слово №{}: ".format(i + 1)))
    while not words[i]:
        words.pop()
        words.append(input("Введите непустое слово №{}: ".format(i + 1)))
    
with open("output.txt", 'w') as f:
    i = 0
    while i < 7:
        f.write("{}{}".format(words[i], words[i + 1]))
        if i != 6:
            f.write("\n")
        i += 2;
