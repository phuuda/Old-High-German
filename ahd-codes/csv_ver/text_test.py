# WILL REWRITE CODE INTO FUNCTIONS LATER

import os
import re
from rules import get_data
from replace_fcns import begin_of_word, after_something, before_r_cons, any_place

# ../../ahd-texts/texts/hildebrandslied.txt

all_rules = get_data('data_table.csv')
f = open('../../ahd-texts/texts/hildebrandslied.txt', 'r', encoding = 'utf-8')
text = f.read()

while '\n' in text:
    text = text.replace('\n', ' ') # BAD FOR ASSEMBLING BACK TEXT LATER

words = text.split(' ')

all_new = []
for word in words:
    changed_word = word
    for rule in all_rules:
        if word: # bypass 'empty' words
            # CONSIDER TEXT-SPECIFIC RULES:
            if (rule['text'] == 'hildebrandslied.txt') or (rule['text'] == 'all'):
            
                if 'в начале слова или после согл.' == rule['placement']:
                    #cw = changed_word
                    changed_word = begin_of_word(changed_word, rule)
                    changed_word = after_something(changed_word, rule)

                    #if cw != changed_word:
                        #print(changed_word, rule['initial'], rule['final'])
                else:
                    if 'в начале слова' == rule['placement']:
                        changed_word = begin_of_word(changed_word, rule)
                    else:
                        if 'после гл.' == rule['placement']:
                            changed_word = after_something(changed_word, rule) 
                        else:                   
                            if 'перед сочетанием r+согл.' == rule['placement']:
                                changed_word = before_r_cons(changed_word, rule)
                            else:
                                if 'любая' == rule['placement']:
                                    changed_word = any_place(changed_word, rule)                                   
                continue
    #print(changed_word, '\n')
    all_new.append(changed_word)
    
print(len(words), len(all_new))
for i in range(len(words)):
    if words[i] != all_new[i]:
        print(words[i], '->', all_new[i])

f.close()
