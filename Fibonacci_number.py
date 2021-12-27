class Solution:
    def better_fibonacci(self, n: int) -> int:
        """
        Returns the nth Fibonacci number in linear time and
        with constant space.
        :param n: Which number to return in the sequence.
        :return: Nth Fibonacci number.
        """
        fib1 = 1
        fib2 = 0
        fib = 0
    
        for num in range(n):
          fib = fib1 + fib2
          fib1 = fib2
          fib2 = fib 
          
        return fib
