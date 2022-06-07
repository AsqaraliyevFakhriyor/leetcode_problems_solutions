# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int):
        start = 1
        end = n
        while start < end:
            mid = (start + end)//2
            if isBadVersion(mid):
                end = mid
            else:
                start = mid + 1
                
        return start

    def firstBadVersion2(self, n) -> int:
        left, right = 1, n
        while left < right:
            mid = left + (right - left) // 2
            if isBadVersion(mid):
                right = mid
            else:
                left = mid + 1
        return left
