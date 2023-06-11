#!/usr/bin/python3
def multiple_returns(sentence):
    """Find the length and first character of a string"""

    length = len(sentence)
    if length:
        return (length, sentence[0])
    return (length, None)
