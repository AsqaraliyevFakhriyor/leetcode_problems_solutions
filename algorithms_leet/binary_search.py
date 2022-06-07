class Solution:
    def search(self, nums, target: int) -> int:
        for n in nums:
            if n == target:
                print(nums.index(n), nums[nums.index(n)])
                return nums.index(n)
        print("-1")
        return -1

    def binary_search(self, nums, target):
        low = 0
        high = len(nums) - 1
        print(high)
        while low <= high:
            middle = (low + high)//2
            guess = nums[middle]
            if nums[middle] == target:
                print(middle)
                return middle
            if guess < target:
                low = middle + 1
            elif guess > target:
                high = middle - 1
        print(-1)
        return -1


list_1 = [-1,0,3,5,9,12]
list_2 = [4, 5, 8, 1, 10, 9, 2, 6, 7]
print(sorted(list_2))
solution = Solution()
solution.binary_search(sorted(list_2), 9)


