# TEST CASE
from rules import get_data
from replace_fcns import begin_of_word, after_something, before_r_cons, any_place

rules = [{'initial': 'th', 'symbol count': 2, 'final': 'd', 'text': 'tatian.txt', 'placement': 'в начале слова'},
         {'initial': 'ó', 'symbol count': 1, 'final': 'o', 'text': 'notker.txt', 'placement': 'любая'},
         {'initial': 'ae', 'symbol count': 2, 'final': 'e', 'text': 'isidor.txt', 'placement': 'перед сочетанием r+согл.'},
         {'initial': 'kch', 'symbol count': 3, 'final': 'k', 'text': 'all', 'placement': 'в начале слова или после согл.'},
         {'initial': 'ch', 'symbol count': 2, 'final': 'hh', 'text': 'all', 'placement': 'после гл.'}]


token1, new_t1 = 'thorn', 'dorn'
res1 = begin_of_word(token1, rules[0])        # BEGIN - WORKS
print(new_t1, res1)
print(new_t1 == res1, '\n')

token2, new_t2 = 'móurn', 'mourn'           # ANY PLACE - WORKS
res2 = any_place(token2, rules[1])
print(new_t2, res2)
print(new_t2 == res2, '\n')

token3, new_t3 = 'aercade', 'ercade'            # BEFORE R + CONS - WORKS
res3 = before_r_cons(token3, rules[2])
print(new_t3, res3)
print(new_t3 == res3, '\n')

token4_1, new_t4_1 = 'kchernel', 'kernel'      # BEGIN - WORKS
res4_1 = begin_of_word(token4_1, rules[3])
print(new_t4_1, res4_1)
print(new_t4_1 == res4_1, '\n')

token4_2, new_t4_2 = 'enkchore', 'enkore'       # AFTER CONS - WORKS 
res4_2 = after_something(token4_2, rules[3])
print(new_t4_2, res4_2)
print(new_t4_2 == res4_2, '\n')

token6, new_t6 = 'echo', 'ehho'                 # AFTER VOWEL - WORKS
res6 = after_something(token6, rules[4])
print(new_t6, res6)
print(new_t6 == res6)
print('\n')

all_rules = get_data('data_table.csv')

all_start = ['thelta', 'môlôkô', 'mólókó', 'mércy', 'mêrcy', 'aercade',
             'dhordher', 'loore', 'cleean', 'bæar', 'parðon', 'pphonpph',
             'kchernel', 'enkchore', 'schone', 'hland', 'afford', 'azzure', 'ahhem',
             'pfopfe', 'phonph', 'zzapzz', 'chomch', 'khlankh', 'scandal', 'hnear',
             'hroad', 'ruf', 'azure', 'ahem', 'mólókó', 'moloko', 'méal', 'meal',
             'zerze', 'klink']

all_end = ['delta', 'môlôkô', 'moloko', 'mercy', 'mêrcy', 'ercade',
           'dorder', 'lôre', 'clêan', 'bêar', 'pardon', 'pfonpf',
           'kernel', 'enkore', 'skone', 'land', 'afford', 'aȥȥure', 'ahhem',
           'pfopfe', 'pfonpf', 'zapz', 'komk', 'klank', 'skandal', 'near',
           'road', 'ruff', 'aȥȥure', 'ahhem', 'môlôkô', 'moloko', 'mêal', 'meal',
           'zerze', 'klink']

all_res = []

for word in all_start:
    changed_word = word
    print(word)

    for rule in all_rules:
        
        if 'в начале слова или после согл.' == rule['placement']:
            changed_word = begin_of_word(changed_word, rule)
            changed_word = after_something(changed_word, rule)
            print(changed_word, '01')

        else:
            if 'в начале слова' == rule['placement']:
                changed_word = begin_of_word(changed_word, rule)
                print(changed_word, '02')

            else:
                if 'после гл.' == rule['placement']:
                    changed_word = after_something(changed_word, rule)
                    print(changed_word, '03')

                else:                   
                    if 'перед сочетанием r+согл.' == rule['placement']:
                        changed_word = before_r_cons(changed_word, rule)
                        print(changed_word, '04')

                    else:
                        if 'любая' == rule['placement']:
                            changed_word = any_place(changed_word, rule)
                            print(changed_word, '04')
        continue
              
    print(changed_word, '\n')
    

print(len(all_start))
print(len(all_end))
print(len(all_res))

