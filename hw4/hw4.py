with open("Tori.txt", encoding="utf-8") as f:
    lines = f.readlines()
    
long_lines_counter = 0
for line in lines:
    if len(line.split()) > 5:
        long_lines_counter += 1

print(round(long_lines_counter / len(lines) * 100), '%')
