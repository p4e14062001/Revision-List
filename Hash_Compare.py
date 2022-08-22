class HashCompare1:
    '''
    https://leetcode.com/problems/bulls-and-cows/
    '''
    def getHint(self, secret: str, guess: str) -> str:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        secF = {}
        gesF = {}
        bulls = 0
        cows = 0
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls = bulls + 1
            else:
                if secret[i] not in secF:
                    secF[secret[i]] = 0
                secF[secret[i]] += 1
                if guess[i] not in gesF:
                    gesF[guess[i]] = 0
                gesF[guess[i]] += 1
        for i in range(10):
            if str(i) in secF and str(i) in gesF:
                cows = cows + min(secF[str(i)], gesF[str(i)])
        return str(bulls) + 'A' + str(cows) + 'B'
