class Greedy1:
    '''
    https://www.interviewbit.com/problems/gas-station/
    '''
	def canCompleteCircuit(self, A, B):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        if sum(A) < sum(B):
            return -1
        start = 0
        sums = 0
        for i in range(len(A)):
            sums = sums + A[i] - B[i]
            if sums < 0:
                start = i + 1
                sums = 0
        return start
class Greedy2:
    '''
    https://leetcode.com/problems/gas-station/
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        if sum(gas) < sum(cost):
            return -1
        diff = [gas[i] - cost[i] for i in range(len(gas))]
        sums = 0
        start = 0
        for i in range(len(diff)):
            sums = sums + diff[i]
            if sums < 0:
                start = i + 1
                sums = 0
        return start
