class IPAddress1:
    '''
    https://leetcode.com/problems/restore-ip-addresses/
    '''
    def restoreIpAddresses(self, s: str) -> List[str]:
        '''
        Time Complexity: O(3 ** N)
        Space Complexity: O(len(s))
        '''
        res = []
        if len(s) > 12:
            return res
        def rec(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return
            for j in range(i, min(i + 3, len(s))):
                if int(s[i:j + 1]) < 256 and (i == j or s[i] != '0'):
                    rec(j + 1, dots + 1, curIP + s[i:j + 1] + ".")
        rec(0, 0, '')
        return res
