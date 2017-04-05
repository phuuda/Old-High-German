def begin_of_word(word, rule):
    n = rule['symbol count']
    normalized_word = word
    
    if normalized_word[:n] == rule['initial']: # consider case sensitivity?
        normalized_word[:n] = rule['final']
            
    return(normalized_word)

def after_something(word, rule):
    n = rule['symbol count']
    normalized_word = word

    vowels = ['a', 'â', 'e', 'ê', 'ë', 'i', 'î',
              'u', 'û', 'ä', 'o', 'ô', 'ö', 'ü']
    
    consonants = ['p', 'b', 'm', 'w', 'f', 'v', 't',
                  'd', 'z', 'n', 's', 'ȥ', 'r', 'l',
                  'c', 'k', 'g', 'h', 'c', 'j']
    k, i, j = 0, 1, n

    if 'после гл.' in rule['placement']:
        letters = vowels
        
    if 'после согл.' in rule['placement']:
        letters = consonants

    while j < len(normalized_word) - 1:
        for c in letters:
            if normalized_word[k] == c:
                if normalized_word[i:j] == rule['initial']:
                    normalized_word[i:j] = rule['final']

        k, i, j = k+1, i+1, j+1
    return(normalized_word)

def before_r_cons(word, rule):
    n = rule['symbol count']
    normalized_word = word
    consonants = ['p', 'b', 'm', 'w', 'f', 'v', 't',
                  'd', 'z', 'n', 's', 'ȥ', 'r', 'l',
                  'c', 'k', 'g', 'h', 'c', 'j']
    i, j, k, m = 0, n-1, j+1, j+2

    while m < len(normalized_word) - 1:
        if normalized_word[k] == 'r':
            for c in consonants:
                if normalized_word[m] == c:
                    if normalized_word[i:j] == rule['initial']:
                        normalized_word[i:j] = rule['final']
        i, j, k, m = i+1, j+1, k+1, m+1
    return(normalized_word)
    
def any_place(word, rule):
    n = rule['symbol count']
    normalized_word = word
    i, j = 0, n-1

    while j < len(normalized_word) - 1:
        if normalized_word[i:j] == rule['initial']:
            normalized_word[i:j] = rule['final']
            
        i, j = i+1, j+1
    return(normalized_word)

# write function that applies all rules in order of 'text', 'symbol count', 'placement' to each word
