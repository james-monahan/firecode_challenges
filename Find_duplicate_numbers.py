

from typing import List


class Solution:
    def find_duplicate_numbers(self, arr: List[int]) -> List[int]:
        """
        Returns duplicate integers in an array as a sorted array.
        :param arr: Input array
        :return: Sorted array of duplicate items from the input
        """
        numbers_seen = set()
        duplicates = set()

        for num in arr:
          if num in numbers_seen:
            duplicates.add(num)
          numbers_seen.add(num)

        return sorted(list(duplicates))
