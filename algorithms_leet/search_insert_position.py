class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if nums.count(target) == 0:
            nums.append(target)
            nums = sorted(nums)
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            guess = nums[mid]
            if guess == target:
                return mid
            if target > guess:
                start = mid + 1
            elif target < guess:
                end = mid - 1
                
                