class Bucket1:
    '''
    https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
    '''
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        '''
        Time Complexity: O(max(max(A), N))
        Space Complexity: O(max(A))
        '''
        f = [0 for _ in range(max(nums) + 1)]
        for i in nums:
            f[i] += 1
        for i in range(1, len(f)):
            f[i] = f[i] + f[i - 1]
        ans = [0 for _ in range(len(nums))]
        for i in range(len(nums)):
            if nums[i] == 0:
                ans[i] = 0
            else:
                ans[i] = f[nums[i] - 1]
        return ans
