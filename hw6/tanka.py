import random
#5
#7
#5
#7
#7

def filework(fname):
    with open(fname, encoding="utf-8") as f:
        text = f.read()
        lines = text.splitlines()
    return random.choice(lines)

def noun1():         #2слога
    filework('nouns1.txt')
    return filework('nouns1.txt')

def adj(word):          #3слога
    filework('adjs.txt')
    return filework('adjs.txt') + ' ' + word

def verb1():         #5слогов
    filework('verbs1.txt')
    return filework('verbs1.txt')

def lm():           #2слога
    filework('lms.txt')
    return filework('lms.txt')

def verb2(word):        #3слога
    filework('verbs2.txt')
    return filework('verbs2.txt') + ' ' + word

def noun2():        #2слога
    filework('nouns2.txt')
    return filework('nouns2.txt')

def lastword():     #7слогов
    filework('lastwords.txt')
    return filework('lastwords.txt')

def tanka():
    tanka = adj(noun1()) + "\n" + verb1()  + ' ' + lm() + "\n" + verb2(noun2()) + "\n" + verb1() + ' ' + noun2() + '...' + "\n" + lastword()
    return tanka

print(tanka())
