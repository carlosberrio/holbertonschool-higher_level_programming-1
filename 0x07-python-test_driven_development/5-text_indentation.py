#!/usr/bin/python3
"""Module for text_indentation method"""


def text_indentation(text):
    """prints a text with 2 new lines after each of these
    characters: '.', '?' and ':'
    Args:
        (str) text: string to be parsed
    Raises:
        TypeError: if text is not a string
    """
    if type(text) is not str:
        raise TypeError('text must be a string')

    for sep in ".?:":
        text = (sep + "\n\n").join([line.strip(" ")
                                    for line in text.split(sep)])

    print(text, end="")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
