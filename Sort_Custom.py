class Sort1:
    '''
    https://leetcode.com/problems/largest-number/
    '''
    def largestNumber(self, nums: List[int]) -> str:
        '''
        Time Complexity: O(N * log(N))
        Space Complexity: O(N)
        '''    
        for i, n in enumerate(nums):
            nums[i] = str(n)
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1
            else:
                return 1
        nums = sorted(nums, key = cmp_to_key(compare))
        return str(int(str(''.join(nums))))
