# Problem statement
# Given a black and white square image, represented as a two dimensional 
# array of integers with values between 0 and 255, write a method that 
# returns a copy of the image, transposed. The transpose of a matrix is 
# an operator which flips a matrix over its diagonal; that is, it switches 
# the row and column indices of the matrix A by producing another matrix, 
# often denoted by AT

from typing import List


class Solution:
    def transpose(self, image: List[List[int]]) -> List[List[int]]:
        """
        Returns the transpose of the input square image.
        :param image: Image as a two dimensional array
        :return: Transposed image.
        """
        transposed = [[None for v in arr] for arr in image]
        idx = len(image)
    
        for i in range(idx):
          for j in range(idx-1, -1, -1):
            transposed[j][i] = image[i][j]
    
    
        return transposed

