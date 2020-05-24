#!/usr/bin/python3
"""Defines a node class"""


class Node:
    """Defines a node"""
    def __init__(self, data, next_node=None):
        """Initializes a node - Constructor
        Args:
            data (int): number to insert in the node
            next_node (Node): pointer to the next node in the chain
        """
        self.data = data
        self.next_node = None

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            if type(value) is not int:
                raise TypeError('data must be an integer')
            self.__data = value

        @property
        def next_node(self):
            return self.__next_node

        @next_node.setter
        def next_node(self, value):
            if value is not None or type(value) is not Node:
                raise TypeError('next_node must be a Node object')
            self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list"""
    def __init__(self):
        """Head points to the first node"""
        self.head = None

    def sorted_insert(self, value):
        """
        Insert node and print the entire list in stdout one value by line
        """
        new = Node(value)
        tmp = self.head
        """Insert node at begginning"""
        if self.head is None or self.head.data > value:
            if self.head:
                new.next_node = self.head
            self.head = new
            return
        """Insert at x position"""
        while tmp.next_node and tmp.next_node.data < value:
            tmp = tmp.next_node
        """If x is not last"""
        if tmp.next_node:
            new.next_node = tmp.next_node
        tmp.next_node = new

    def __str__(self):
        """
        self method that converts list to string and prints it
        in stdout one value by line
        """
        list_str = ""
        node = self.head
        while node:
            list_str += str(node.data) + '\n'
            node = node.next_node
        return list_str[:-1]
