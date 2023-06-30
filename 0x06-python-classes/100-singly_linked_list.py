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
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Create the singlyLinkedList"""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new node into a linked list in a sorted manner"""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            temp = self.__head
            prev = None
            while temp is not None and temp.data < value:
                prev = temp
                temp = temp.next_node
            if prev is None:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                prev.next_node = new_node
                new_node.next_node = temp

    def __str__(self):
        """Print linked list data line by line"""
        temp = self.__head
        linked_list = ""
        while temp:
            linked_list += str(temp.data) + "\n"
            temp = temp.next_node
        return linked_list.strip()
