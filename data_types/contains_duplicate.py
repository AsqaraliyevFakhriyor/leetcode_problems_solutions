class Solution:

    def __init__(self, nums):
        self.nums = nums

    def dp_set_method(self):
        """Finding if list has duplicates with help of sets in python"""
        if len(self.nums) == len(set(self.nums)):
            print("No dp!")
            return False
        else:
            print("has dp!")
            return True

    def dp_set(self):
        """finding duplicates with set, you can use lists too :)"""
        dp = set()
        for n in self.nums:
            if n in dp:
                print("Has dp!")
                return True
            else:
                dp.add(n)
        print("No dp!")
        return False

    def dp_count(self):
        """finding duplicates with count list method"""
        for n in self.nums:
            if self.nums.count(n) > 1:
                print("Has dp!")
                return True
        print("No dp!")
        return False

    def my_ans(self):
        """Simple!, Cean! and Readable :)"""
        n = len(self.nums)
        for j in range(n):
            for i in range(j+1, n):
                print(j, i)
                if self.nums[j] == self.nums[i]:
                    print("Has dp!")
                    return True
        print("No dp!")
        return False
                    
            

solution = Solution([6,1,2,4,5,6])
print(solution.my_ans())

        