# WIP

from rules import get_data
from replace_fcns import begin_of_word, after_something, before_r_cons, any_place

def txt_to_word_list(txt_file):
    f = open(txt_file, 'r', encoding = 'utf-8')
    text = f.read()
    word_list = []

    for x in text:
        word_list.append(x)
    f.close()

    return word_list

rules = get_data('data_table.csv')


def iterate_rules(word, rule):
    changed_word = word
    
    if 'после гл.' in rule['placement']:
        changed_word = after_something(changed_word, rule)
                
    if 'после согл.' in rule['placement']:
        changed_word = after_something(changed_word, rule)
                
    if 'перед сочетанием r+согл.' in rule['placement']:
        changed_word = before_r_cons(changed_word, rule)
                
    if 'в начале слова' in rule['placement']:
        changed_word = begin_of_word(changed_word, rule)
                
    if 'любая' in rule['placement']:
        changed_word = any_place(changed_word, rule)    

    return changed_word

def apply_rules(text_file, word, rules):

    for rule in rules:
        if rule['text'] == 'all':
            changed_word = iterate_rules(word, rule)
        
        if text_file == rule['text']:
            changed_word = iterate_rules(word, rule)

    return changed_word
   

