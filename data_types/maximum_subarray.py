class FindSubArray:
    """Takes array and retturns sum of biggest subarray in given array, methods: max_subarr_kadens_algorithm, simple_way"""

    def __init__(self, arr):
        self.arr = arr

    def max_subarr_kadens_algorithm(self):
        "finding biggest subarray with kades algorithms"
        n = len(self.arr)
        for j in range(1, n):
            if self.arr[j-1] > 0:
                self.arr[j] += self.arr[j-1]
        return max(self.arr)

    def simple_way(self):
        """Simple way of finding biggest subarrays """
        n = len(self.arr)
        max_sum = -1e8
        for j in range(n):
            current_sum = 0

            # calculating subarrays
            for i in range(j, n):
                current_sum += self.arr[i]

                # Checking if its bigger than our max value
                # if its, we changing max_sum value to current_sum
                if current_sum > max_sum:
                    max_sum = current_sum
        return max_sum
