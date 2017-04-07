# WIP

def begin_of_word(word, rule):      # consider case sensitivity?
    n = rule['symbol count']
    normalized_word = word
    if normalized_word[:n] == rule['initial']:
        normalized_word = normalized_word.replace(normalized_word[:n], rule['final'])

    return(normalized_word)

def after_something(word, rule):
    n = rule['symbol count']
    normalized_word = word

    vowels = ['a', 'â', 'e', 'ê', 'ë', 'i', 'î',
              'u', 'û', 'ä', 'o', 'ô', 'ö', 'ü']
    consonants = ['p', 'b', 'm', 'w', 'f', 'v', 't',
                  'd', 'z', 'n', 's', 'ȥ', 'r', 'l',
                  'c', 'k', 'g', 'h', 'c', 'j']
    k = 0
    i = k+1
    j = k+1+n

    if 'после гл.' in rule['placement']:
        letters = vowels
        
    if 'после согл.' in rule['placement']:
        letters = consonants

    while j <= len(normalized_word):
        for c in letters:
            if normalized_word[k] == c:
                if normalized_word[i:j] == rule['initial']:
                    if len(rule['initial']) == 1:               # preserves 'hh'/'ff' for rule 'h -> hh'/'f -> ff'
                        if len(rule['final']) == 2:
                            if rule['final'][0] == rule['final'][1]:
                                if normalized_word[i:j+1] == rule['final']:
                                    pass
                                else:
                                    normalized_word = normalized_word.replace(normalized_word[k+1:k+n+1], rule['final'])
        k += 1
        i += 1
        j += 1

    return(normalized_word)

def before_r_cons(word, rule):
    n = rule['symbol count']
    normalized_word = word
    consonants = ['p', 'b', 'm', 'w', 'f', 'v', 't',
                  'd', 'z', 'n', 's', 'ȥ', 'r', 'l',
                  'c', 'k', 'g', 'h', 'c', 'j']
    i = 0
    j = n
    k = n
    m = n+1

    while m < len(normalized_word):
        if normalized_word[k] == 'r':
            for c in consonants:
                if normalized_word[m] == c:
                    if normalized_word[i:j] == rule['initial']:
                        normalized_word = normalized_word.replace(normalized_word[i:j], rule['final'])
        i += 1
        j += 1
        k += 1
        m += 1
    return(normalized_word)

def any_place(word, rule):
    n = rule['symbol count']
    normalized_word = word
    i = 0
    j = n

    while j < len(normalized_word):
        if normalized_word[i:j] == rule['initial']:
            normalized_word = normalized_word.replace(rule['initial'], rule['final'])
        i += 1
        j += 1
    return(normalized_word)

