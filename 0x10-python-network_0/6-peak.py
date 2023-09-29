#!/usr/bin/python3
"""Module to find a PEAK"""


def find_peak(list_of_integers):
    """Calculate the peak"""
    if list_of_integers:
        length = len(list_of_integers)
        cur_peak = max(list_of_integers)
        new_peak = 0
        for i in range(0, (length // 2 + length // 3)):
            if (i != 0 and i != length - 1):
                if (list_of_integers[i] > list_of_integers[i + 1]):
                    if (list_of_integers[i] > list_of_integers[i - 1]):
                        if list_of_integers[i] > new_peak:
                            if list_of_integers[i] != cur_peak:
                                new_peak = list_of_integers[i]
        if new_peak != 0:
            return new_peak
        return cur_peak

    return None
