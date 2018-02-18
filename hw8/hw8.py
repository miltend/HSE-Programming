import random

def read_dict(fname):
    d = {}
    with open(fname, encoding='utf-8') as f:
        text = f.read()
    for line in text.splitlines():
        cell = line.split(';')
        d[cell[0]] = cell[1]
    return d

def hint(d):
    word = random.choice(list(d.keys()))
    user_input = input(word + '... ')
    if user_input == d[word]:
        print(random.choice(('nice one!', 'good job!', 'well done!')))
    else:
        print(random.choice(('nope :(', 'unfortunately, no', 'unlucky!')))

def main():
    hint(read_dict('2gramms.csv'))

main()
