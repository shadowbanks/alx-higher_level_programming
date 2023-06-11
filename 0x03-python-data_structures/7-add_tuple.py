#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples"""
    if len(tuple_a) < 2:
        tuple_a = tuple_a[:2] + (0,) * (2 - len(tuple_a))
    else:
        tuple_a = tuple_a[:2]
    if len(tuple_b) < 2:
        tuple_b = tuple_b[:2] + (0,) * (2 - len(tuple_b))
    else:
        tuple_b = tuple_b[:2]
    return tuple(x+y for x, y in zip(tuple_a, tuple_b))
