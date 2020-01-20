#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/19 11:35 上午
@Author  : duanpy001
@File    : 17.py
@Link    : https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_char_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                         '9': 'wxyz'}
        res = []
        # 组合问题
        def combination(prefix, next_digit):
            if next_digit == '':
                res.append(prefix)
            else:
                for letter in num_char_dict[next_digit[0]]:
                    combination(prefix + letter, next_digit[1:])

        if len(digits) == 0:
            return []
        combination('', digits)
        return res

    def letterCombinations_2(self, digits: str) -> List[str]:
        num_char_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv',
                             '9': 'wxyz'}
        if len(digits) == 0:
            return []
        # dp[i]表示前 i 个字母的所有组合
        dp = [[] for _ in range(len(digits))]
        dp[0] = list(num_char_dict[digits[0]])
        for i in range(1, len(digits)):
            dp[i] = [prefix + letter for prefix in dp[i-1] for letter in num_char_dict[digits[i]]]
        return dp[-1]


if __name__ == '__main__':
    s = Solution()
    test_data = ['23']
    test_res = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
    for i in test_data:
        print(s.letterCombinations_2(i))
