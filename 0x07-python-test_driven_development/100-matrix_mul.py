#!/usr/bin/python3
"""
This module ```100-matrix_mul``` multiplies two matrixes
"""


def matrix_mul(m_a, m_b):
    """
    Multiply two matrixes while handliing necessary errors
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if (len(m_a) > 0 and not all(isinstance(x, list) for x in m_a)):
        raise TypeError("m_a must be a list of lists")
    if (len(m_b) > 0 and not all(isinstance(x, list) for x in m_b)):
        raise TypeError("m_b must be a list of lists")
    if (not len(m_a) > 0 or not all(len(x) > 0 for x in m_a)):
        raise ValueError("m_a can't be empty")
    if (not len(m_b) > 0 or not all(len(x) > 0 for x in m_b)):
        raise ValueError("m_b can't be empty")
    if not all(isinstance(x, (int, float)) for rows in m_a for x in rows):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(x, (int, float)) for rows in m_b for x in rows):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(x) == len(m_a[0]) for x in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(x) == len(m_b[0]) for x in m_b):
        raise TypeError("each row of m_b must be of the same size")
