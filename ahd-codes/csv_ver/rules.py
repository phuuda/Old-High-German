from operator import itemgetter
import csv

##class Rule:
##    def __init__(self, start, end, where):
##        self.start = start
##        self.end = end
##        self.where = where
##    def __str__(self):
##        return '{} {} {}'.format(self.start, self.end, self.where)

def get_data(fileName):
    infile = open(fileName, 'r', encoding='utf-8')
    table = [] # data from csv file
    for row in csv.reader(infile):
        table.append(row)
    infile.close()
    
    data = []
    number = 1
    for row in table:
        start = row[1] # old grapheme
        end = row[5] # change to this
        where = row[4] # position
        fn = row[6] # .txt file
        count = len(start) # grapheme symbol count
        
        if number != 1:
            if fn:
#                if len(start) == 1:
#                    print(ord(start)) # convert char to its ASCII value
#                    print(chr(240)) # unicode integer to character


                data_element = {'text': fn, 'initial': start, 'final': end, 'placement': where, 'symbol count': count}


            if not fn:
                fn = 'all' # RULES WITH NO INFO ON WHICH TEXT
                data_element = {'text': fn, 'initial': start, 'final': end, 'placement': where, 'symbol count': count}

            if data_element['placement'] != '': # don't add rules with unspecified 'placement'
                if data_element: # don't add empty or WIP 'initial' rules
                    initial_check = data_element['initial']
                    if initial_check != '':
                        if '?' not in initial_check:
                            if '(' not in initial_check:
                                data.append(data_element)
        number += 1

    sorted_data = sorted(data, key = itemgetter('text', 'symbol count', 'placement'), reverse = True)
    return sorted_data


if __name__ == '__main__':
    for line in get_data('data_table.csv'):
        print(line)
