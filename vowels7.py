def search4vowels(word:str) -> set:
    """Display any vowels found in a supplied word"""

    vowels = set('aeiou')
    return vowels.intersection(set(word))



