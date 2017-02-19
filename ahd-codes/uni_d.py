# -*- coding: utf-8 -*-


def all_reps(filename, reps):
    f = open(filename, 'r')
    text = f.read()
    print(text)
    f.close()
    for k, v in reps.items():
        text = text.replace(k, v)
    f = open(filename.replace('.txt', '_result.txt'), 'w')
    f.write(text)
    f.close()

data = {
    'isidor.txt':{'dh': 'd', 'Dh': 'D'},
    'tatian.txt':{' th': ' d', ' Th': ' D', 'Th': 'D', '\nth': '\nd'},
    'hildebrandslied.txt':{'Г°': 'd', 'Гђ': 'D'}
    # место для добавления новых текстов и заменяемых граф. обозначений
    # (?) в дальнейшем возможно выделение диалектов, где замены для неск-ких языков общие
}

for k, v in data.items():
    all_reps(k, v)

