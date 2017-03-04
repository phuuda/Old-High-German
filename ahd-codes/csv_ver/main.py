from rules import get_data
from uni_d import all_reps

if __name__ == '__main__':
    for file_name, rule in get_data('data_table.csv').items():
        all_reps(file_name, {rule.start: rule.end})