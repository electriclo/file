def is_anagram(a_word, b_word):
    """
    >>> is_anagram("abc", "acb")
    True
    >>> is_anagram("silent", "listen")
    True
    >>> is_anagram("one", "two")
    False
    >>> is_anagram("anagram", "nag a ram")
    True
    """
    return sorted(a_word) == sorted(b_word)

    # i ran the doctest by writing "python -m doctest -v joyce_q3.py"
    # the error is that the program expected True but got False
    # to fix the error, i need to write False instead of True on the 10th line
    