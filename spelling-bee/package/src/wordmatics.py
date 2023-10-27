def filter(word, allowed, required):
    if len(word) < 4:
        return False
    rf = False
    for letter in word:
        if letter.lower() == required.lower():
            rf = True
        if letter.lower() not in allowed.lower() and letter.lower() != required.lower():
            return False
    return rf


def pangram(word, letters, center):
    """
    returns a boolean of whether the selected word is a pangram containing all input letters
    
    params:
    (str) word -- word to check
    (str) letters -- list of chars to check
    (char) center -- center letter required by spelling be to match formatting

    returns:
    True - the word contains all specified letters
    False - the word is not a pangram
    """
    if not center in word:
        return False
    for l in letters:
        if not l in word:
            return False
    return True

def valid_words_list():
    with open('../resources/dict', 'r') as source_file:
        words = source_file.read().split()
    return words

def all_words_list():
    with open('../resources/words', 'r') as source_file:
        words = source_file.read().split()
    return words