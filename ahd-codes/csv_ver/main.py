from rules import get_data
from uni_d import all_reps, write_in_file
import os

if __name__ == '__main__':
    filepath = '../../ahd-texts/texts/'
    for file in os.listdir(filepath):
        if '_result.txt' not in file:
            print('{} in process'.format(file))
            newpath = os.path.join(filepath, file)
            words, all_new = all_reps(file, newpath)
            write_in_file(newpath, words, all_new)
    '''
    for file_name, rule in get_data('data_table.csv').items():
        all_reps(file_name, {rule.start: rule.end})
        '''
