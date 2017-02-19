# -*- coding: utf-8 -*-

#не можем точно найти большую ð

def all_reps(filename, reps):
    f = open(filename, 'r')
    text = f.read()
    f.close()
    for k, v in reps.items():
        text = text.replace(k, v)
    f = open(filename.replace('.txt', '_result.txt'), 'w')
    f.write(text)
    f.close()

data = {
    'isidor.txt':{'dh': 'd', 'Dh': 'D'},
    'tatian.txt':{' th': ' d', ' Th': ' D', 'Th': 'D', '\nth': '\nd'},
    'hildebrandslied.txt':{'Г°': 'd'}
    #место для файлов и символов замен
}

for k, v in data.items():
    all_reps(k, v)