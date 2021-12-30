# Problem statement
# Given the head DoubleLinkListNode of a doubly linked list and an integer, 
# write a method to insert a new node with the given integer as its data to 
# the head of the list. Return the head of the modified list.

from DoubleLinkListNode import DoubleLinkListNode


class Solution:
    def insert_at_head(self, head: DoubleLinkListNode, n: int) -> DoubleLinkListNode:
        """
        Inserts a new ListNode with data n to the tail of the singly linked list,
        given the head of the list.
        :param head: Head of the doubly linked list.
        :param n: Integer to set on the data property of the inserted node.
        :return: Head DoubleLinkListNode of the modified double linked list.
        """
        
        node = head 
        first_node = DoubleLinkListNode(n)
        if node == None:
            return first_node
            
        head.previous = first_node
        first_node.next = head
        return first_node
