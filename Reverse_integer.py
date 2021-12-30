# Problem statement
# Write a method that reverses an input integer, with constant space complexity.

class Solution:
    def reverse(self, input: int) -> int:
        """
        Reverses the input integer with constant space complexity.
        :param input: Input integer to be reversed.
        :return: Reversed integer.
        """
        number = input 
        reversed_num = 0
        
        while number > 0:
            reversed_num = (reversed_num * 10) + number % 10
            number = number // 10
            
        return reversed_num
