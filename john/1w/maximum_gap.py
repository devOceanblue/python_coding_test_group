class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lo, hi, n = min(nums), max(nums), len(nums)
        if n <= 2 or hi == lo: return hi - lo
        bucket_max = [0] * n
        bucket_min = [10**9+1] * n
        for num in nums:
            ind = n-2 if num == hi else (num - lo)*(n-1)//(hi-lo)
            bucket_max[ind] = max(num, bucket_max[ind])
            bucket_min[ind] = min(num, bucket_min[ind])
        
        maxgap = 0
        # consider min
        previous = lo
        for i in range(n-1):
            if bucket_min[i] == 10**9+1 and bucket_max[i] == 0:
                #empty bucket
                continue
            maxgap = max(maxgap, bucket_min[i] - previous)
            previous = bucket_max[i]
        #consider max
        maxgap = max(maxgap, hi - previous)
        return maxgap
