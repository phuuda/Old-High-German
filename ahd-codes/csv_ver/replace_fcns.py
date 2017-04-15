# WIP

def preserve_case(word, normalized_word): # applied in all functions below
    word = str(word)
            
    if word[0].isupper(): # Word
        normalized_word = normalized_word.replace(normalized_word[0], normalized_word[0].upper())

    if word.isupper(): # WORD
        normalized_word = normalized_word.isupper()

    return normalized_word

def begin_of_word(word, rule):
    i = 0
    if (word[0] == '«') or (word[0] == '\"') or (word[0] == '\('):
        i = 1

    n = rule['symbol count']
    word = str(word)
    normalized_word = word.lower()

    if normalized_word[i:n] == rule['initial']:
        normalized_word = normalized_word.replace(normalized_word[i:n], rule['final'])

    #normalized_word = preserve_case(word, normalized_word)
    return(normalized_word)

def after_something(word, rule):
    n = rule['symbol count']
    word = str(word)
    normalized_word = word.lower()

    vowels = ['a', 'â', 'ä', 'e', 'ę', 'ê', 'ë', 'i', 'î',
              'u', 'û', 'ü', 'o', 'ô', 'ö']
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
                    if len(rule['initial']) == 1:   # preserve 'hh' for rule 'h -> hh'
                        if len(rule['final']) == 2:
                            if rule['final'][0] == rule['final'][1]:    # rule['final'] == 'hh'
                                if normalized_word[i:j+1] == rule['final']: # 'hh' == hh'
                                    pass
                                
                                if j < len(normalized_word): # preserve 'zz' for rule 'z' -> 'ȥȥ'
                                    if normalized_word[i:j] == normalized_word[j]:
                                        pass
                                    else:
                                        normalized_word = normalized_word.replace(normalized_word[k+1:k+n+1], rule['final'])
                                else:
                                    normalized_word = normalized_word.replace(normalized_word[k+1:k+n+1], rule['final'])
                    else:
                        normalized_word = normalized_word.replace(normalized_word[k+1:k+n+1], rule['final'])                           
        k += 1
        i += 1
        j += 1

    #normalized_word = preserve_case(word, normalized_word)
    return(normalized_word)

def before_r_cons(word, rule):
    n = rule['symbol count']
    word = str(word)
    normalized_word = word.lower()
    
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
        
    #normalized_word = preserve_case(word, normalized_word)
    return(normalized_word)

def any_place(word, rule):
    n = rule['symbol count']
    word = str(word)
    normalized_word = word.lower()
    i = 0
    j = n

    while j < len(normalized_word):
        if normalized_word[i:j] == rule['initial']:
            normalized_word = normalized_word.replace(rule['initial'], rule['final'])
        i += 1
        j += 1
        
    #normalized_word = preserve_case(word, normalized_word)
    return(normalized_word)

