class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        if not nums:
            return 0
        
        for i in range(len(nums)):
            if target <= nums[i]:
                return i
        return i + 1
        