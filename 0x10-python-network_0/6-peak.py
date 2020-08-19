#!/usr/bin/python3
"""Module that finds a peak in a list of unsorted integers."""


def findPeak(array, left, right):
    """Aux Method"""
    if left == right:
        return array[left]
    mid = int((left + right) / 2)
    if array[mid] < array[mid + 1]:
        return findPeak(array, mid + 1, right)
    return findPeak(array, left, mid)


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if not list_of_integers:
        return
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    if list_of_integers[1] <= list_of_integers[0]:
        return list_of_integers[0]
    if list_of_integers[-1] >= list_of_integers[-2]:
        return list_of_integers[-1]
    return findPeak(list_of_integers, 0, len(list_of_integers) - 1)
