class Geometry1:
    '''
    https://leetcode.com/problems/minimum-time-visiting-all-points/
    '''
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        ans = 0
        def time(x1, x2, y1, y2):
            return max(abs(x1 - x2), abs(y1 - y2))
        for i in range(1, len(points)):
            ans += time(points[i][0], points[i - 1][0], points[i][1], points[i - 1][1])
        return ans
