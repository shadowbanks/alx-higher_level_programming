#!/usr/bin/python3

"""Create a singly linked list"""


class Node:
    """Create a node for singly linked list"""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")

    @property
    def next_node(self):
        return self.__next_node
    @next_node.setter
    def next_node(self, value):
        if value not None or not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Create the singlyLinkedList"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        temp = self.__head
        new_node
