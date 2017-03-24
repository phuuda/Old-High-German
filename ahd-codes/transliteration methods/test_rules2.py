import re
#2 способ с помощью регулярных выражений

#не надо разбивать на графемы
word1 = 'adalihueth'
word2 = 'eete'
word_final_test = 'adaliuettuhatheete'
#должно получиться othaligueth

#правила записываем как раньше только в виде регулярок
#Просто выставляем правила по порядку (важен порядок - это минус этого способа)
rules = [
    (r'ada', r'atha'),
    (r'^a', r'o'),
    (r'([^t])(h)', r'\1g'), #не t а потом h
    #(r'e', r'!'), #так будет неправильно
    (r'ee', r'E'),
    (r'e', r'E'),
]

word = word_final_test
print(word)

for rule in rules:
    start = rule[0]
    end = rule[1]
    #заменяем через re.sub
    word = re.sub(start, end, word)

print(word)

#print(re.sub(r'([^t])(h)', r'\1g', 'adalihueth'))