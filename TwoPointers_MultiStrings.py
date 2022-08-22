class TwoPointers1:
    '''
    https://leetcode.com/problems/backspace-string-compare/
    '''
    def backspaceCompare(self, s: str, t: str) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        sp = len(s) - 1
        tp = len(t) - 1
        sskips = 0
        tskips = 0
        while sp > -1 or tp > -1:
            while sp > -1:
                if s[sp] == '#':
                    sskips += 1
                    sp = sp - 1
                elif sskips > 0:
                    sp = sp - 1
                    sskips = sskips - 1
                else:
                    break
            while tp > -1:
                if t[tp] == '#':
                    tskips += 1
                    tp = tp - 1
                elif tskips > 0:
                    tp = tp - 1
                    tskips = tskips - 1
                else:
                    break
            if sp > -1 and tp > -1 and s[sp] != t[tp]:
                return False
            if (sp > -1) != (tp > -1):
                return False
            sp = sp - 1
            tp = tp - 1
        return True
