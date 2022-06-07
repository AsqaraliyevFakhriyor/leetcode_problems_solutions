class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        new_nums = []
        for n in nums:
            new_nums.append((n)**2)
            
        return sorted(new_nums)
        
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            nums[i] = (n)**2
        nums.sort()
        return nums
        