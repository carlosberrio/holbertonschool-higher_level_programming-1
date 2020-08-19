#!/usr/bin/python3
""" Test function find_peak """


def find_peak(list_of_integers):
    """Testing"""
    if len(list_of_integers) == 0:
        return None
    peak = list_of_integers[0]
    for n in list_of_integers:
        if n > peak:
            peak = n
    return peak
