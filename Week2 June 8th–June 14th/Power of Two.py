class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n >= 1:
            if n == float(1):
                return True
            n = n / 2
        return False
            
        