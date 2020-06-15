class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        d = {}
        
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
                
        for i in range(len(nums)):
            if 0 in d and d[0] != 0:
                nums[i] = 0
                d[0] -= 1
            elif 1 in d and d[1] != 0:
                nums[i] = 1
                d[1] -= 1
            elif 2 in d and d[2] != 0:
                nums[i] = 2
                d[2] -= 1
                
        
        