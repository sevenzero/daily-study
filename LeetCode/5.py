#!/usr/bin/env python 
# -*- coding: utf-8 -*-
"""
@Time    : 2020/1/10 10:23
@Author  : duanpy001
@File    : 5.py
@Link    : https://leetcode-cn.com/problems/longest-palindromic-substring/
"""


class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        max_s = ''
        if n <= 1:
            return s
        for i in range(1, n):
            p, q = i - 1, i + 1
            while p >= 0 and q < n:
                if s[p] != s[q]:
                    break
                p -= 1
                q += 1
            max_s = max(max_s, s[p + 1:q], key=len)
        for i in range(0, n):
            p, q = i, i + 1
            while p >= 0 and q < n:
                if s[p] != s[q]:
                    break
                p -= 1
                q += 1
            max_s = max(max_s, s[p + 1:q], key=len)
        return max_s

    def longestPalindrome_2(self, s: str) -> str:
        n = len(s)
        max_s = ''
        if n <= 1:
            return s
        p = [False] * n
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, i - 1, -1):
                p[j] = ((j - i < 2) | p[j - 1]) & (s[i] == s[j])
                if p[j]:
                    max_s = max(max_s, s[i:j + 1], key=len)
        return max_s


if __name__ == '__main__':
    s = Solution()
    test_data = ['a', 'aa', 'aba', 'abc', 'abba', 'abbc', 'abbac']
    for i in test_data:
        print(s.longestPalindrome_2(i))
