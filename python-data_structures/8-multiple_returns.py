#!/usr/bin/python3
def multiple_returns(sentence):
    sen_len = len(sentence)
    char = ''
    if not sentence:
        char = None
    else:
        char = sentence[0]
    return(sen_len, char)

