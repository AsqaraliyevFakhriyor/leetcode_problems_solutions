import time

class Solution:
    def rotate_double_loop(self, nums: list, k: int):
        """
        Time complexity: 0(n*k) used double loop used so 2*n
        Space complexity: 0(1)
        """
        for _ in k:
            last_item = nums[-1]
            for i in range(len(nums)):
                nums[i], last_item = last_item, nums[i]
            
    def rotate_extra_array(self, nums: list, k: int):
        extra_arr = [0] * len(nums)
        n = len(nums)
        print("len(nums): ", n)
        for i in range(len(nums)):
            extra_arr[(i+k) % n] = nums[i]
            # we are using % n to recycle indexes
            # or index will increases until 9 and
            # will raise exception out of index 

        # nums[:] = extra_arr[:]
        for i in range(len(nums)):
            nums[i] = extra_arr[i]
        print(nums)
        return nums


    def rotate_cyclic_replacements(self, nums, k):
        """
        
        Time complexity : O(n). Only one pass is used.
        Space complexity : O(1). Constant extra space is used.

        """
        k = k % len(nums)
        count = 0
        start = 0
        while count < len(nums):
            current = start 
            prev = nums[start] #store the value in the position
            
            while True:
                next = (current + k) % len(nums) #
                temp = nums[next] #store it temporaly 
                nums[next] = prev #overide the next 
                prev = temp #reset prev
                current = next #reset current
                count += 1

                if start == current:
                    break 
            
            start += 1

    def rotate_using_reverse(self, nums, k) -> None:
        """
        
        Time complexity : O(n) .nnelements are reversed a total of three times.
        Space complexity : O(1). No extra space is used.

        """
        k %= len(nums)
        self.reverse(nums,0,len(nums)-1)
        self.reverse(nums,0, k-1)
        self.reverse(nums,k, len(nums)-1)

    def reverse(self, nums, start, end) -> None:
        """
        :type nums: List[int]
        :type start: int
        :type end: int
        :rtype: None
        """
        while start < end: #
            temp = nums[start]
            nums[start] = nums[end]
            nums[end] = temp 
            start += 1
            end -= 1


test1 = Solution()
t1  = time.perf_counter()
test1.rotate_extra_array([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
t2 = time.perf_counter()

print("Time: ", t2-t1)