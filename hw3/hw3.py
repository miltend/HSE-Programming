a = input('Input string:\n')
while a == '':
    a = input('Input string!:\n')
print('Output:\n', a)
while len(a) > 2:
    a = a[1: len(a) - 1]
    print(a)
