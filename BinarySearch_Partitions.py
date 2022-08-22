class BinarySearch1:
    '''
    https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1
    '''
    def findPages(self,A, N, M):
        '''
        Time Complexity: O(N * log(N))
        Space Complexity: O(1)
        '''
        def allocation(barrier):
            '''
            Time Complexity: O(N)
            Space Complexity: O(1)
            '''
            st = 1
            pages = 0
            for i in range(len(A)):
                if A[i] > barrier:
                    return False
                if pages + A[i] > barrier:
                    st = st + 1
                    pages = arr[i]
                else:
                    pages = pages + arr[i]
            if st > M:
                return False
            return True
        low = min(A)
        high = sum(A)
        res = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            if allocation(mid):
                res = mid
                high = mid - 1
            else:
                low = mid + 1
        return low
class BinarySearch2:
    '''
    https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
    '''
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        Time Complexity: O(N * log(N))
        Space Complexity: O(1)
        '''
        def alloc(mid):
            '''
            Time Complexity: O(N)
            Space Complexity: O(1)
            '''
            d = 1
            w = 0
            for i in range(len(weights)):
                if weights[i] > mid:
                    return False
                if w + weights[i] > mid:
                    d = d + 1
                    w = weights[i]
                else:
                    w = w + weights[i]
            if d > days:
                return False
            return True
        low = min(weights)
        high = sum(weights)
        while low <= high:
            mid = low + (high - low) // 2
            if alloc(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
class BinarySearch3:
    '''
    https://leetcode.com/problems/split-array-largest-sum/
    '''
    def splitArray(self, nums: List[int], m: int) -> int:
        '''
        Time Complexity: O(N * log(N))
        Space Complexity: O(1)
        '''
        def alloc(mid):
            '''
            Time Complexity: O(N)
            Space Complexity: O(1)
            '''
            s = 0
            parts = 1
            for i in range(len(nums)):
                if nums[i] > mid:
                    return False
                if s + nums[i] > mid:
                    parts = parts + 1
                    s = nums[i]
                else:
                    s = s + nums[i]
            if parts > m:
                return False
            return True
        low = min(nums)
        high = sum(nums)
        while low <= high:
            mid = low + (high - low) // 2
            if alloc(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
class BinarySearch4:
    '''
    https://www.codingninjas.com/codestudio/problems/painter's-partition-problem_1089557
    '''
    def findLargestMinDistance(boards:list, k:int):
        '''
        Time Complexity: O(N * log(N))
        Space Complexity: O(1)
        '''
        def alloc(mid):
            '''
            Time Complexity: O(N)
            Space Complexity: O(1)
            '''
            parts = 1
            paint = 0
            for i in range(len(boards)):
                if boards[i] > mid:
                    return False
                if paint + boards[i] > mid:
                    parts = parts + 1
                    paint = boards[i]
                else:
                    paint = paint + boards[i]
            if parts > k:
                return False
            return True
        low = min(boards)
        high = sum(boards)
        while low <= high:
            mid = low + (high - low) // 2
            if alloc(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low
