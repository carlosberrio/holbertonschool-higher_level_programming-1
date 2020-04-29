#!/usr/bin/python3
def remove_char_at(str, n):
    newString = ""
    for idx, ch in enumerate(str):
        if idx != n:
            newString += ch
    return newString
