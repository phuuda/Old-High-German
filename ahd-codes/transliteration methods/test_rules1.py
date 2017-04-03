word1 = 'adaliuettt'
word2 = 'hath'
word3 = 'eete'
word_final_test = 'adaliuettuhatheete'



# 1 способ с представлением
# 1) Проблема - как разбить слово на графемы

#допустим есть список графем
GRAFEM_LIST = [
    'th',
    'ee',
    'sch',
    #важен порядок графем, e должно быть после ee
    'e'
]

def get_grafems(word):
    # с первым словом всё ок - просто делим по буквам
    #return list(word)
    # со вторым словом надо как то понять что th - это отдельная графема
    # по крайней мере нужен список всех графем (трудно будет разбить)
    #идем по списку графем
    for number, grafem in enumerate(GRAFEM_LIST):
        word = word.replace(grafem, str(number))

    word_list = list(word)
    for number, grafem in enumerate(GRAFEM_LIST):
        for i in range(len(word_list)):
            val = word_list[i]
            if val == str(number):
                word_list[i] = grafem

    return word_list



# 2) Проблема в том, что для каждого правила придется писать свою функцию (сложная функция)
# функция которая заменяет все начальные а на o
def start_a_to_o(start, result):
    '''start и result - Это списки из графем'''
    start_letter = start[0]
    if start_letter == 'a':
        result[0] = 'o'


# все d между a заменяем на th
def all_d_to_th(start, result):
    for i in range(len(start)):
        letter = start[i]
        if letter == 'd' and i != 0 and i != len(start) - 1 and start[i - 1] == 'a' and start[i + 1] == 'a':
            result[i] = 'th'


def ee_to_e(start, result):
    for i in range(len(start)):
        letter = start[i]
        if letter == 'ee':
            result[i] = 'E'


def e_to_e(start, result):
    for i in range(len(start)):
        letter = start[i]
        if letter == 'e':
            result[i] = 'E'


def h_to_g_not_th(start, result):
    for i in range(len(start)):
        letter = start[i]
        if i==0 and letter == 'h':
            #заменяем
            result[i] = 'g'
        if i > 0 and letter == 'h' and start[i-1] != 't':
            result[i] = 'g'


old_word = word_final_test
start = get_grafems(old_word)
print(start)
#При разбиении на графемы тоже надо будет учитывать порядок

# берем копию чтобы списки были разные
result = start[:]

# набор правил будет выглядеть как список методов
# Плюс в том, что правила можно применять в любом
rules = [
    all_d_to_th,
    start_a_to_o,
    e_to_e,
    ee_to_e,
    h_to_g_not_th,
]

for rule in rules:
    rule(start, result)

print(result)

