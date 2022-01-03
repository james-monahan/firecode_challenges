# Problem statement
# Given the head node of a linked list, write a method that recursively deletes its nth node 
# and returns the head of the modified list. If n exceeds the bounds of the linked list, 
# return the list without any modifications. See the provided ListNode interface for available methods.

from ListNode import ListNode


class Solution:
    def delete_at_index(self, head: ListNode, n: int) -> ListNode:
        """
        Recursively deletes the node at the nth index of the input linked
        list. If n is out of bounds, returns the list without
        modification.
        :param head: Head of the singly linked list.
        :param n: Index (zero-indexed) of the node to be deleted.
        :return: Head ListNode of the modified linked list.
        """
        if head == None:
            return None
            
        if n == 0:
            return head.next
            
        head.next = self.delete_at_index(head.next, n - 1)
            
            
        return head
