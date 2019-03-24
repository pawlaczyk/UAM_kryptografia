#coding=utf-8

"""
Jako ułomny dyslektyk robię sobie pliki ze słowami  literowymi 1, 2,3,4,5
jeszcze tylko mapuję słowa ą -> a i tworzę takie pliki

potem spróbuję dopasować litery na podstawie słów - pomapuję, bo ręczne łamigłówki zabiły moją moc obliczeniową o.Ó
(chyba scrable są nie dla mnie)


https://sjp.pl/slownik/growy/
"""

word_1 = []
word_2 =[]
word_3 = []
word_4 = []
word_5 = []

# switch_case = {
#     1: lambda x: word_1.append(x),
#     2: lambda x: word_2.append(x),
#     3: lambda x: word_3.append(x),
#     4: lambda x: word_4.append(x),
#     5: lambda x: word_5.append(x)
# }
#
#
# def emulate_switch_case(word_length, word):
#     switch_case.get(word_length, lambda:None)()


with open('polish_dictionary.txt', 'r') as f:
    for line in f:
        line = line.replace("\n", "")
        if len(line) == 1:
            word_1.append(line)
        if len(line) == 2:
            word_2.append(line)
        if len(line) == 3:
            word_3.append(line)
        if len(line) == 4:
            word_4.append(line)
        if len(line) == 5:
            word_5.append(line)


with open("1.txt", "w") as f:
    f.write(' '.join(word_1))


with open("2.txt", "w") as f:
    f.write(' '.join(word_2))


with open("3.txt", "w") as f:
    f.write(' '.join(word_3))


with open("4.txt", "w") as f:
    f.write(' '.join(word_4))


with open("5.txt", "w") as f:
    f.write(' '.join(word_5))
