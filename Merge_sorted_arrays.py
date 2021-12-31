# Problem statement
# Merge sort is a classic divide and conquer algorithm that 
# recursively divides an input array in two halves, sorts each half, 
# then merges those two halves. Write a method that accepts two sorted 
# arrays, merges them and returns a new globally sorted array, 
# comprised of all elements of the input arrays.

from typing import List


class Solution:
    def merge_sorted(self, arr1: List[int], arr2: List[int]) -> List[int]:
        """
        Merges two sorted arrays.
        :param arr1: First sorted array.
        :param arr2: Second sorted array.
        :return: Merged sorted array.
        """
        if len(arr1) == 0 or len(arr2) == 0:
          return arr1 + arr2
    
        sorted_array = [None] * (len(arr1)+len(arr2))
        arr1_index = 0
        arr2_index = 0
    
        for i in range(len(sorted_array)):
          arr1_is_exhasted = not arr1_index < len(arr1) 
          arr2_is_exhasted = not arr2_index < len(arr2)
    
          if (not arr1_is_exhasted) and (arr2_is_exhasted or arr1[arr1_index] <= arr2[arr2_index]):
            sorted_array[i] = arr1[arr1_index]
            arr1_index += 1
    
          else:
            sorted_array[i] = arr2[arr2_index]
            arr2_index += 1
    
        return sorted_array
