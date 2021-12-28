# Problem statement
# Given an array of integers and an integer target, 
# write a method to find and return the indices of two numbers 
# that sum up to the target integer. The output should be an 
# array containing the two indices, with the first index < the second.

# -There will be at most one such pair in the input array.
# -if no such pair is found, return an empty array.
# -The output array should be sorted in ascending order.
# -Target linear time and space complexity.

from typing import List


class Solution:
    def two_sum(self, arr: List[int], target: int) -> List[int]:
        """
        Takes in an integer list and a target number and returns
        an integer list containing indices of numbers that add up to
        the target number.
        :param arr: Integer list.
        :param target: Integer target.
        :return: Indices of numbers which add up to the target number.
        """
        check_for_num = set(arr)
        indexes = []
        match = 0
    
        for i,v in enumerate(arr):
          if len(indexes) == 2:
            return indexes
          pair = target-v
          if pair in check_for_num:
            indexes.append(i)
            match = pair
          if v == match:
            if i != indexes[-1]:
              indexes.append(i) 
            if i == indexes[-1]:
              indexes.pop()
    
        return indexes 
