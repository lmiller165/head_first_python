def search4vowels(phrase:str) -> set:
    """Display any vowels found in a supplied word"""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))


def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Take in a phrase and return True if the asked for letter in there"""
    return set(letters).intersection(set(phrase))
