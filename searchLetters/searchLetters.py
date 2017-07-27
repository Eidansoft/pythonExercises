
def search4vowels(phrase):
    """Return any vowel found at the phrase passed as argument"""
    vowels=set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase, letters):
    """Return the letters present at the letters argument and the phrase argument"""
    return set(letters).intersection(set(phrase))
