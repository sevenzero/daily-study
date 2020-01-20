#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/20 11:41 上午
@Author  : duanpy001
@File    : 22.py
@Link    : https://leetcode-cn.com/problems/generate-parentheses/
"""
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(seq=[]):
            if len(seq) == 2 * n:
                if valid(seq):
                    ans.append("".join(seq))
            else:
                seq.append('(')
                generate(seq)
                seq.pop()
                seq.append(')')
                generate(seq)
                seq.pop()

        def valid(seq):
            left = 0
            for c in seq:
                if c == '(':
                    left += 1
                else:
                    left -= 1
                if left < 0:
                    return False
            return left == 0

        ans = []
        generate()
        return ans

    def generateParenthesis_2(self, n: int) -> List[str]:
        res = []
        def backtrack(prefix, left, right):
            if len(prefix) == 2 * n:
                res.append(prefix)
                return
            if left < n:
                backtrack(prefix + '(', left + 1, right)
            if right < left:
                backtrack(prefix + ')', left, right + 1)
        backtrack('', 0, 0)
        return res

    def generateParenthesis_3(self, n: int) -> List[str]:
        dp = [[] for _ in range(n + 1)]
        dp[0] = ['']
        for i in range(1, n + 1):
            for p in range(i):
                left = dp[p]
                right = dp[i-1 - p]
                for left_seq in left:
                    for right_seq in right:
                        dp[i].append('(' + left_seq + ')' + right_seq)
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    print(s.generateParenthesis_3(0))
