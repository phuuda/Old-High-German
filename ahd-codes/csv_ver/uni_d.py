from rules import get_data
import re
from replace_fcns import begin_of_word, after_something, before_r_cons, any_place

def all_reps(filename, filepath):
    all_rules = get_data('data_table.csv')
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()

    while '\n' in text:
        text = text.replace('\n', ' ')  # BAD FOR ASSEMBLING BACK TEXT LATER

    words = text.split(' ')

    all_new = []
    for word in words:
        changed_word = word
        for rule in all_rules:
            if word:  # bypass 'empty' words
                # CONSIDER TEXT-SPECIFIC RULES:
                if (rule['text'] == filename) or (rule['text'] == 'all'):

                    if 'в начале слова или после согл.' == rule['placement']:
                        # cw = changed_word
                        changed_word = begin_of_word(changed_word, rule)
                        changed_word = after_something(changed_word, rule)

                        # if cw != changed_word:
                        # print(changed_word, rule['initial'], rule['final'])
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
        # print(changed_word, '\n')
        all_new.append(changed_word)

    f.close()
    return words, all_new

def write_in_file(filename, words, all_new):
    f = open(filename, 'r', encoding = 'utf-8')
    text = f.read()
    f.close()
    for i in range(len(words)):
        text = text.replace(' ' + words[i] + ' ', ' ' + all_new[i] + ' ')
        text = text.replace(' ' + words[i] + '\n', ' ' + all_new[i] + '\n')
        text = text.replace('\n' + words[i] + ' ', '\n' + all_new[i] + ' ')
    f = open(filename.replace('.txt', '_result.txt'), 'w', encoding = 'utf-8')
    f.write(text)
    f.close()

if __name__ == '__main__':
    words, all_new = all_reps('hildebrandslied.txt')
    print(words)
    print(all_new)
    write_in_file('../../ahd-texts/texts/hildebrandslied.txt', words, all_new)
