#сколько в тексте слов с приставкой un- (слова типа uncle тоже можно считать)
#и какой процент из них имеет длину большую, чем число, введенное пользователем
#(если пользователь ввел число 5, то какой процент слов с приставкой
#un- длиннее 5 символов).

def filename():
    fname = input('введите название файла  :')
    return fname

def words_from_text(fname):
    try:
        with open(fname, encoding='utf-8') as f:
            text = f.read()
        text = text.lower()
        symbols_to_remove = """,.:;'"(-<>)"""
        for s in symbols_to_remove:
            text = text.replace(s, '')
        words = text.split()
        return words
    except FileNotFoundError:
        print('такого файла нет')
        return None

def un_words(words):
    unstuff = {}
    a = 1
    if words is not None:
        if words:
            for x in words:
                if x.startswith('un'):
                    unstuff.update({a: x})
                a += 1
            return unstuff
        else:
            print('в файле нет слов')
    else:
        pass

def user_number():
    is_input_ok = False
    while not is_input_ok:
        try:
            number = int(input('введите число  :'))
            if number <= 0:
                s_input_ok = False
                print('invalid input')
            else:
                is_input_ok = True
        except ValueError:
            print('invalid input')
    return number  

def percent(number, dictionary):
    a = 0
    b = 0
    if dictionary is not None:
        if dictionary:
            for word in dictionary.values():
                a += 1
                if len(word) > number:
                    b += 1
            print(round(b/a *100), '%')
        else:
            print('слов, начинающихся на un- нет')
    else:
        pass

def main():
    percent(user_number(), un_words(words_from_text(filename())))

main()           


