class BuySellStock1:
    '''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
    '''
    def maxProfit(self, arr: List[int]) -> int:
        def prefix():
            '''
            Time Complexity: O(N - 1)
            Space Complexity: O(2)
            '''
            mini = arr[0]
            profit = 0
            for i in range(1, len(arr)):
                profit = max(profit, arr[i] - mini)
                mini = min(mini, arr[i])
            return profit
        return prefix()
class BuySellStock2:
    '''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
    '''
    def maxProfit(self, prices: List[int]) -> int:
        def rec(index, status):
            '''
            Time Complexity: O(2 ** N)
            Space Complexity: O(N)[Auxillary Stack Space]
            '''
            if index == len(prices):
                return 0
            if status == 0:
                buy = -prices[index] + rec(index + 1, 1)
                not_buy = 0 + rec(index + 1, 0)
                return max(buy, not_buy)
            else:
                sell = prices[index] + rec(index + 1, 0)
                not_sell = 0 + rec(index + 1, 1)
                return max(sell, not_sell)
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        def mem(index, status):
            '''
            Time Complexity: O(N * 2)
            Space Complexity: O(N * 2) + O(N)[Auxillary Stack Space]
            '''
            if index == len(prices):
                return 0
            if dp[index][status] != -1:
                return dp[index][status]
            if status == 0:
                buy = -prices[index] + mem(index + 1, 1)
                not_buy = 0 + rec(index + 1, 0)
                dp[index][status] = max(buy, not_buy)
                return dp[index][status]
            else:
                sell = prices[index] + mem(index + 1, 0)
                not_sell = 0 + rec(index + 1, 1)
                dp[index][status] = max(sell, not_sell)
                return dp[index][status]
        def tab():
            '''
            Time Complexity: O((N + 1) * 2)
            Space Complexity: O((N + 1) * 2)
            '''
            dp = [[-1 for _ in range(2)] for _ in range(len(prices) + 1)]
            for index in range(len(prices), -1, -1):
                for status in range(1, -1, -1):
                    if index == len(prices):
                        dp[len(prices)][status] = 0
                    else:
                        if status == 0:
                            buy = -prices[index] + dp[index + 1][1]
                            not_buy = 0 + dp[index + 1][0]
                            dp[index][status] = max(buy, not_buy)
                        else:
                            sell = prices[index] + dp[index + 1][0]
                            not_sell = 0 + dp[index + 1][1]
                            dp[index][status] = max(sell, not_sell)
            return dp[0][0]
        def opt():
            '''
            Time Complexity: O((N + 1) * 2)
            Space Complexity: O(2 * 2)
            '''
            prev = [-1 for _ in range(2)]
            for index in range(len(prices), -1, -1):
                curr = [-1 for _ in range(2)]
                for status in range(1, -1, -1):
                    if index == len(prices):
                        curr[status] = 0
                    else:
                        if status == 0:
                            buy = -prices[index] + prev[1]
                            not_buy = 0 + prev[0]
                            curr[status] = max(buy, not_buy)
                        else:
                            sell = prices[index] + prev[0]
                            not_sell = 0 + prev[1]
                            curr[status] = max(sell, not_sell)
                prev = curr
            return prev[0]
        return opt()
        return tab()
        return mem(0, 0)
        return rec(0, 0)
class BuySellStock3:
    '''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
    '''
    def maxProfit(self, prices: List[int]) -> int:
        def rec(index, status):
            '''
            Time Complexity: O(2 ** N)
            Space Complexity: O(N)[Auxillary Stack Space]
            '''
            if status == 4:
                return 0
            elif index == len(prices):
                return 0
            elif status % 2 == 0:
                buy = -prices[index] + rec(index + 1, status + 1)
                not_buy = 0 + rec(index + 1, status)
                return max(buy, not_buy)
            elif status % 2 == 1:
                sell = prices[index] + rec(index + 1, status + 1)
                not_sell = 0 + rec(index + 1, status)
                return max(sell, not_sell)
        dp = [[-1 for _ in range(4)] for _ in range(len(prices))]
        def mem(index, status):
            '''
            Time Complexity: O(N * 4)
            Space Complexity: O(N * 4) + O(N)[Auxillary Stack Space]
            '''
            if status == 4:
                return 0
            elif index == len(prices):
                return 0
            elif dp[index][status] != -1:
                return dp[index][status]
            elif status % 2 == 0:
                buy = -prices[index] + mem(index + 1, status + 1)
                not_buy = 0 + mem(index + 1, status)
                return max(buy, not_buy)
            elif status % 2 == 1:
                sell = prices[index] + mem(index + 1, status + 1)
                not_sell = 0 + mem(index + 1, status)
                return max(sell, not_sell)
        def tab():
            '''
            Time Complexity: O((N + 1) * 5)
            Space Complexity: O((N + 1) * 5)
            '''
            dp = [[-1 for _ in range(5)] for _ in range(len(prices) + 1)]
            for index in range(len(prices), -1, -1):
                for status in range(4, -1, -1):
                    if index == len(prices):
                        dp[index][status] = 0
                    elif status == 4:
                        dp[index][status] = 0
                    else:
                        if status % 2 == 0:
                            buy = -prices[index] + dp[index + 1][status + 1]
                            not_buy = 0 + dp[index + 1][status]
                            dp[index][status] = max(buy, not_buy)
                        else:
                            sell = prices[index] + dp[index + 1][status + 1]
                            not_sell = 0 + dp[index + 1][status]
                            dp[index][status] = max(sell, not_sell)
            return dp[0][0]
        def opt():
            '''
            Time Complexity: O((N + 1) * 5)
            Space Complexity: O(5 * 2)
            '''
            prev = [-1 for _ in range(5)]
            for index in range(len(prices), -1, -1):
                curr = [-1 for _ in range(5)]
                for status in range(4, -1, -1):
                    if index == len(prices):
                        curr[status] = 0
                    elif status == 4:
                        curr[status] = 0
                    else:
                        if status % 2 == 0:
                            buy = -prices[index] + prev[status + 1]
                            not_buy = 0 + prev[status]
                            curr[status] = max(buy, not_buy)
                        else:
                            sell = prices[index] + prev[status + 1]
                            not_sell = 0 + prev[status]
                            curr[status] = max(sell, not_sell)
                prev = curr
            return prev[0]
        return opt()
        return tab()
        return mem(0, 0)
        return rec(0, 0)
class BuySellStock4:
    '''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/
    '''
    def maxProfit(self, k: int, prices: List[int]) -> int:
        k = 2 * k
        def rec(index, status):
            '''
            Time Complexity: O(2 ** N)
            Space Complexity: O(N)[Auxillary Stack Space]
            '''
            if index == len(prices) or status == k:
                return 0
            elif status % 2 == 0:
                buy = -prices[index] + rec(index + 1, status + 1)
                not_buy = 0 + rec(index + 1, status)
                return max(buy, not_buy)
            else:
                sell = prices[index] + rec(index + 1, status + 1)
                not_sell = 0 + rec(index + 1, status)
                return max(sell, not_sell)
        dp = [[-1 for _ in range(k)] for _ in range(len(prices))]
        def mem(index, status):
            '''
            Time Complexity: O(N * k)
            Space Complexity: O(N * k) + O(N)[Auxilary Stack Space]
            '''
            if index == len(prices) or status == k:
                return 0
            if dp[index][status] != -1:
                return dp[index][status]
            elif status % 2 == 0:
                buy = -prices[index] + mem(index + 1, status + 1)
                not_buy = 0 + mem(index + 1, status)
                dp[index][status] = max(buy, not_buy)
                return dp[index][status]
            else:
                sell = prices[index] + mem(index + 1, status + 1)
                not_sell = 0 + mem(index + 1, status)
                dp[index][status] = max(sell, not_sell)
                return dp[index][status]
        def tab():
            '''
            Time Complexity: O((N + 1) * (k + 1))
            Space Complexity: O((N + 1) * (k + 1))
            '''
            dp = [[-1 for _ in range(k + 1)] for _ in range(len(prices) + 1)]
            for index in range(len(prices), -1, -1):
                for status in range(k, -1, -1):
                    if status == k or index == len(prices):
                        dp[index][status] = 0
                    elif status % 2 == 0:
                        buy = -prices[index] + dp[index + 1][status + 1]
                        not_buy = 0 + dp[index + 1][status]
                        dp[index][status] = max(buy, not_buy)
                    else:
                        sell = prices[index] + dp[index + 1][status + 1]
                        not_sell = 0 + dp[index + 1][status]
                        dp[index][status] = max(sell, not_sell)
            return dp[0][0]
        def opt():
            '''
            Time Complexity: O((N + 1) * (k + 1))
            Space Complexity: O(2 * (k + 1))
            '''
            prev = [-1 for _ in range(k + 1)]
            for index in range(len(prices), -1, -1):
                curr = [-1 for _ in range(k + 1)]
                for status in range(k, -1, -1):
                    if status == k or index == len(prices):
                        curr[status] = 0
                    elif status % 2 == 0:
                        buy = -prices[index] + prev[status + 1]
                        not_buy = 0 + prev[status]
                        curr[status] = max(buy, not_buy)
                    else:
                        sell = prices[index] + prev[status + 1]
                        not_sell = 0 + prev[status]
                        curr[status] = max(sell, not_sell)
                prev = curr
            return prev[0]
        return opt()
        return tab()
        return mem(0, 0)
        return rec(0, 0)
class BuySellStock5:
    '''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
    '''
    def maxProfit(self, prices: List[int]) -> int:
        def rec(index, status):
            '''
            Time Complexity: O(2 ** N)
            Space Complexity: O(N)[Auxillary Stack Space]
            '''
            if index >= len(prices):
                return 0
            if status == 0:
                buy = -prices[index] + rec(index + 1, 1)
                not_buy = rec(index + 1, 0)
                return max(buy, not_buy)
            else:
                sell = prices[index] + rec(index + 2, 0)
                not_sell = rec(index + 1, 1)
                return max(sell, not_sell)
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        def mem(index, status):
            '''
            Time Complexity: O(N * 2)
            Space Complexity: O(N)[Auxillary Stack Space]
            '''
            if index >= len(prices):
                return 0
            if status == 0:
                buy = -prices[index] + mem(index + 1, 1)
                not_buy = mem(index + 1, 0)
                dp[index][status] = max(buy, not_buy)
                return dp[index][status]
            else:
                sell = prices[index] + mem(index + 2, 0)
                not_sell = mem(index + 1, 1)
                dp[index][status] = max(sell, not_sell)
                return dp[index][status]
        def tab():
            '''
            Time Complexity: O((N) * 2)
            Space Complexity: O((N + 2) * 2)
            '''
            dp = [[0 for _ in range(2)] for _ in range(len(prices) + 2)]
            for index in range(len(prices), -1, -1):
                for status in range(1, -1, -1):
                    if index == len(prices):
                        dp[index][status] = 0
                    elif status == 0:
                        buy = -prices[index] + dp[index + 1][1]
                        not_buy = dp[index + 1][0]
                        dp[index][status] = max(buy, not_buy)
                    else:
                        sell = prices[index] + dp[index + 2][0]
                        not_sell = dp[index + 1][1]
                        dp[index][status] = max(sell, not_sell)
            return dp[0][0]
        return tab()
        return mem(0, 0)
        return rec(0, 0)
class BuySellStock6:
    '''
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/
    '''
    def maxProfit(self, prices: List[int], fee: int) -> int:
        def rec(index, status):
            '''
            Time Complexity: O(2 ** N)
            Space Complexity: O(N)[Auxillary Stack Space]
            '''
            if index == len(prices):
                return 0
            if status == 0:
                buy = -prices[index] + rec(index + 1, 1)
                not_buy = rec(index + 1, 0)
                return max(buy, not_buy)
            if status == 1:
                sell = prices[index] + rec(index + 1, 0) - fee
                not_sell = rec(index + 1, 1)
                return max(sell, not_sell)
        dp = [[-1 for _ in range(2)] for _ in range(len(prices))]
        def mem(index, status):
            '''
            Time Complexity: O(N * 2)
            Space Compelxity: O(N)[Auxillary Stack Space]
            '''
            if index == len(prices):
                return 0
            if dp[index][status] != -1:
                return dp[index][status]
            if status == 0:
                buy = -prices[index] + mem(index + 1, 1)
                not_buy = mem(index + 1, 0)
                dp[index][status] = max(buy, not_buy)
                return dp[index][status]
            if status == 1:
                sell = prices[index] + mem(index + 1, 0) - fee
                not_sell = mem(index + 1, 1)
                dp[index][status] = max(sell, not_sell)
                return dp[index][status]
        def tab():
            '''
            Time Complexity: O((N + 1) * 2)
            Space Complexity: O((N + 1) * 2)
            '''
            dp = [[0 for _ in range(2)] for _ in range(len(prices) + 1)]
            for index in range(len(prices), -1, -1):
                for status in range(1, -1, -1):
                    if index == len(prices):
                        dp[index][status] = 0
                    else:
                        if status == 0:
                            buy = -prices[index] + dp[index + 1][1]
                            not_buy = dp[index + 1][0]
                            dp[index][status] = max(buy, not_buy)
                        if status == 1:
                            sell = prices[index] + dp[index + 1][0] - fee
                            not_sell = dp[index + 1][1]
                            dp[index][status] = max(sell, not_sell)
            return dp[0][0]
        def opt():
            '''
            Time Complexity: O((N + 1) * 2)
            Space Complexity: O(2 * 2)
            '''
            prev = [0 for _ in range(2)]
            for index in range(len(prices), -1, -1):
                curr = [0 for _ in range(2)]
                for status in range(1, -1, -1):
                    if index == len(prices):
                        curr[status] = 0
                    else:
                        if status == 0:
                            buy = -prices[index] + prev[1]
                            not_buy = prev[0]
                            curr[status] = max(buy, not_buy)
                        if status == 1:
                            sell = prices[index] + prev[0] - fee
                            not_sell = prev[1]
                            curr[status] = max(sell, not_sell)
                prev = curr
            return prev[0]
        return opt()
        return tab()
        return mem(0, 0)
        return rec(0, 0)
