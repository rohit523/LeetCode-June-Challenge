class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        
        if not nums:
            return []
        
        dp = [0] * len(nums)
        
        dp[0] = [nums[0]]
        
        nums.sort()
        
        for i in range(1, len(nums)):
            maxset = []
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dp[j]) > len(maxset):
                        maxset = dp[j].copy()
            dp[i] = maxset
            dp[i].append(nums[i])

        return max(dp, key=len)
        
        
            
            
        