#!/usr/bin/python3
def roman_to_int(roman_string):

    if isinstance(roman_string, str) is False:
        return 0

    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    value = 0
    for n in range(len(roman_string)-1):
        if romans[roman_string[n]] >= romans[roman_string[n+1]]:
            value = value + romans[roman_string[n]]
        else:
            value = value - romans[roman_string[n]]
    value = value + romans[roman_string[-1]]
    return value
