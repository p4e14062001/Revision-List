class GreedySort1:
    '''
    https://practice.geeksforgeeks.org/problems/maximize-sum-after-k-negations1149/1
    '''
    def maximizeSum(self, a, n, k):
        '''
        Time Complexity: O(N * log(N))
        Space Complexity: O(1)
        '''
        a.sort()
        flag = 0
        for i in range(n):
            if a[i] < 0:
                if k > 0:
                    a[i] = -a[i]
                    k = k - 1
                else:
                    flag = 1
                    break
        if flag == 1:
            return sum(a)
        if k % 2 == 0:
            return sum(a)
        return sum(a) - 2 * min(a)
