#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        x = None
    else:
        x = sentence[0]
    return (len(sentence), x)
