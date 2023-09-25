def pangram(word, letters, center):
    if not center in word:
        return False
    for l in letters:
        if not l in word:
            return False
    return True