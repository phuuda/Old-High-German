from rules import get_data
import os # new stuff

def all_reps(filename, reps):

    for root, dirs, files in os.walk('.'): # new stuff
        for i in files:
            if i == filename:

                f = open(filename, 'r', encoding='utf-8')
                text = f.read()
                print(text)
                f.close()
                for k, v in reps.items():
                    text = text.replace(k, v)
                f = open(filename.replace('.txt', '_result.txt'), 'w', encoding='utf-8')
                f.write(text)
                f.close()

if __name__ == '__main__':
    for file_name, rule in get_data('data_table.csv').items():
        all_reps(file_name, {rule.start: rule.end})
