import csv

class Rule:
    def __init__(self, start, end, where):
        self.start = start
        self.end = end
        self.where = where
    def __str__(self):
        return '{} {} {}'.format(self.start, self.end, self.where)

def get_data(fileName):
    infile = open(fileName, 'r', encoding='utf-8')
    table = []
    for row in csv.reader(infile):
        table.append(row)
    infile.close()
    data = {}
    number = 1
    for row in table:
        start = row[1]
        end = row[5]
        where = row[4]
        fn = row[6]
        if number != 1:
            if fn:
                print(start)
                if len(start) == 1:
                    print(ord(start))
                    print(chr(240))
                data[fn] = Rule(start, end, where)
        number += 1
    return data
if __name__ == '__main__':
    for k, v in get_data('data_table.csv').items():
        print(k, v)