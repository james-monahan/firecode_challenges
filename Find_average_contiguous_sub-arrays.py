# Problem statement
# Given an array of n integers and an integer k, find the average of all contiguous subarrays of size k in it. 
# While the brute force approach will yield a time complexity of O(n * k), try to accomplish this with a time complexity of O(n).

from typing import List, Mapping


class Solution:
    def averages(self, arr: List[int], k: int) -> List[float]:
        """
        Returns the average of all contiguous sub-lists
        of size k in the given integer array, starting with
        the first element.
        :param arr: Integer list.
        :param k: Number of contiguous elements in the sub-list.
        :return: List of averages.
        """
        left = 0
        _sum = 0
        averages = []
    
        for right in range(len(arr)):
          _sum += arr[right]
    
          if right + 1 >= k:
            averages.append(_sum/k)
            _sum -= arr[left]
            left += 1
    
        return averages
